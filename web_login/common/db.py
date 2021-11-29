# -- coding: utf-8 --
import pymysql
from common.conf import Conf
def read_sqls(sqlfile):
    file=open('../initsqls/'+sqlfile, 'r', encoding='utf-8')
    sqls=[] # 存所有的sql语句
    for sql in file: # file中有很多行，sql是其中一行
        if not sql.startswith('--'):
            sqls.append(sql.strip())
    return sqls
class DB:
    def __init__(self):
        dbinfo=Conf().dbinfo
        self.conn=pymysql.connect(**dbinfo)
        self.cursor=self.conn.cursor() # 游标
    def init_db(self,sqlfile):
        sqls=read_sqls(sqlfile)
        for sql in sqls:
            self.cursor.execute(sql)
        self.conn.commit() # 保存数据到数据库
        self.conn.close()
if __name__ == '__main__':
    # print(read_sqls('login.sql'))
    DB().init_db('login.sql')