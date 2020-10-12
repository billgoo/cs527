# -- encoding: utf-8 --

"""
@author: Yan Gu
@Date:
"""

import boto3
import sys
from DBManager.database_manager import DatabaseManager


"""connect to s3"""
s3 = boto3.resource('s3')
bucket = s3.Bucket('instacartforcs527')

"""connect to RDS"""
mydb = DatabaseManager()

for obj in bucket.objects.all():
    key = obj.key
    """aisles table"""
    if key == 'aisles.csv':
        mydb.cursor.execute('DROP TABLE IF EXISTS aisles')
        mydb.cursor.execute('''CREATE TABLE aisles (aisle_id INT NOT NULL ,aisle VARCHAR(256) NOT NULL ,PRIMARY KEY (aisle_id));''')
        body = obj.get()['Body'].read()
        content = str(body)
        lines = content.split("\\r\\n")
        print('Copying '+ str(len(lines)-2) + ' lines...')
        for num in range(len(lines)-1):
            if num == 0:
                continue
            item = lines[num].split(',')
            
            mydb.cursor.execute('''INSERT INTO aisles (aisle_id, aisle)
                        VALUES (%s,%s)''', (item[0],item[1]))
            mydb.conn.commit()
        print('Copy successfully!')
mydb.cursor.close()
