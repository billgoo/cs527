# -- encoding: utf-8 --

"""
@author: Yan Gu
@Date:
"""

import boto3
from collections import OrderedDict
import sys

from loguru import logger

from DBManager.database_manager import DatabaseManager


# sql dict for all sql query
SQL_DICT = OrderedDict({
    # "aisles.csv": {
    #     "DROP": ("DROP TABLE IF EXISTS aisles"),
    #     "CREATE": ("""CREATE TABLE aisles (
    #         aisle_id INT NOT NULL, aisle VARCHAR(256) NOT NULL,
    #         PRIMARY KEY (aisle_id))"""),
    #     "INSERT": ("""INSERT INTO aisles ( aisle_id, aisle )
    #         VALUES ( %s, %s )""")
    # },
    # "departments.csv": {
    #     "DROP": ("DROP TABLE IF EXISTS departments"),
    #     "CREATE": (
    #         """CREATE TABLE departments (
    #         department_id INT NOT NULL,
    #         department VARCHAR (256) NOT NULL,
    #         PRIMARY KEY (department_id))"""
    #     ),
    #     "INSERT": ("""INSERT INTO departments ( department_id, department )
    #         VALUES ( %s, %s )""")
    # },
    # "orders.csv": {
    #     "DROP": ("DROP TABLE IF EXISTS orders"),
    #     "CREATE": (
    #         """CREATE TABLE orders (
    #         order_id INT NOT NULL,
    #         user_id INT NOT NULL,
    #         order_number INT NOT NULL,
    #         order_dow INT NOT NULL,
    #         order_hour_of_day INT NOT NULL,
    #         days_since_prior_order INT NOT NULL,
    #         PRIMARY KEY (order_id))"""
    #     ),
    #     "INSERT": ("""INSERT INTO orders (
    #             order_id, user_id, order_number, order_dow,
    #             order_hour_of_day, days_since_prior_order
    #         )
    #         VALUES ( %s, %s, %s, %s, %s, %s )"""
    #     )
    # },
    "products.csv": {
        "DROP": ("DROP TABLE IF EXISTS products"),
        "CREATE": (
            """CREATE TABLE products (
                product_id INT NOT NULL,
                product_name VARCHAR (256) NOT NULL,
                aisle_id INT NOT NULL,
                department_id INT NOT NULL,
                PRIMARY KEY (product_id),
                CONSTRAINT pd_aidfk_1 FOREIGN KEY (aisle_id) REFERENCES aisles(aisle_id),
                CONSTRAINT pd_didfk_1 FOREIGN KEY (department_id) REFERENCES departments(department_id)
            )"""
        ),
        "INSERT": ("""INSERT INTO products ( product_id, product_name, aisle_id, department_id )
            VALUES ( %s, %s, %s, %s )""")
    },
    "order_products.csv": {
        "DROP": ("DROP TABLE IF EXISTS order_products"),
        "CREATE": (
            """CREATE TABLE order_products (
                order_id INT NOT NULL,
                product_id INT NOT NULL,
                add_to_cart_order INT NOT NULL,
                reordered INT NOT NULL,
                PRIMARY KEY ( product_id, order_id ),
                CONSTRAINT opd_pidfk_1 FOREIGN KEY (product_id) REFERENCES products(product_id),
                CONSTRAINT opd_oidfk_1 FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )"""
        ),
        "INSERT": (
            """INSERT INTO order_products (
            order_id, product_id, add_to_cart_order, reordered
            ) VALUES (
                %s, %s, %s, %s
            )"""
        )
    }
})

# connect to s3
s3 = boto3.resource('s3')
bucket = s3.Bucket('instacartforcs527')
# get all obj from s3
obj_dict = {obj.key: obj for obj in bucket.objects.all()}

# read data from s3 obj and write data into rds
for key, value in SQL_DICT.items():
    logger.info("key on s3: {}".format(key))

    # read data from s3 obj
    obj = obj_dict[key]
    body = obj.get()['Body'].read()
    content = str(body, encoding="utf-8")   # decode bytes str
    lines = content.split("\r\n") # split lines in str
    logger.info("Read in total {0} lines of data from table {1}".format(
        len(lines) - 2, str(key).split(".")[0]))

    # connect to RDS
    mydb = DatabaseManager()
    # init table
    mydb.cursor.execute(value["DROP"])
    mydb.cursor.execute(value["CREATE"])

    # write data into rds
    logger.info("Start writing in total {0} lines of data into table {1}".format(
        str(len(lines) - 2), str(key).split(".")[0]))
    for i in range(len(lines) - 1):
        columns = tuple(lines[i].split(","))
        mydb.cursor.execute(value["INSERT"], columns)
        # mydb.conn.commit()
        if i % 2000 == 0:
            logger.info("Write {0} lines.".format(i))
            mydb.conn.commit()

    mydb.conn.commit()
    logger.info("Write successfully!")

    mydb.cursor.close()
    mydb.conn.close()
