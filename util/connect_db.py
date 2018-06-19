__author__ = 'Administrator'
import json

import pymysql


class OperationMySQL(object):
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def search_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        result = json.dumps(result)
        return result

    def search(self, key, i):
        self.cursor.execute("select " + str(key) + " from testcase")
        results = self.cursor.fetchall()
        # print(results[1][key])
        # result = json.dumps(result)
        # print(len(results))
        return results[i][key]

    def write(self, key, id):
        self.cursor.execute("update testcase set result='" + str(key) + "' where id='" + str(id) + "'")
        self.conn.commit()


    def update(self):
        self.cursor.execute("update testcase set result='pass' where id='Imooc-01'")
        self.conn.commit()

    def get_count(self):
        self.cursor.execute("select count(*) from testcase")
        rows_count = self.cursor.fetchall()
        return rows_count[0]['count(*)']

if __name__ == '__main__':
    op_db = OperationMySQL()
    # res = op_db.search_one("select * from user where userName='litianle'")
    # print(res)
    print(op_db.search('url', 1))
    print(op_db.write('pass', 'Imooc-01'))
    print(op_db.get_count())

