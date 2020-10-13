import pymysql
from time import time
import re

def buildQueryFromInput(raw_query):
    return re.sub('\s+', ' ', raw_query)

class connect_mysql():
    def __init__(self, host, user, password, db, port):
        self.db = pymysql.connect(host=host, user=user, password=password, db=db, port=port)
        self.cursor = self.db.cursor()

    def make_query(self, query):
        start_time = int(round(time() * 1000))
        self.cursor.execute(query)
        col_info = self.cursor.description
        result = self.cursor.fetchall()
        query_time = str(int(round(time() * 1000)) - start_time) + " ms"
        if len(result) > 100:
            result = result[:99]
        col_name = []
        for i in range(len(col_info)):
            col_name.append(col_info[i][0])
        return col_name, result, query_time

    def disconnect(self):
        self.db.close()