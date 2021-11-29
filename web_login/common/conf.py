# -- coding: utf-8 --
import configparser
class Conf:
    def __init__(self):
        self.read_db_conf()
        self.read_server_conf()
    def read_server_conf(self):
        conf=configparser.ConfigParser()
        conf.read('../conf/server.conf')
        protocol=conf.get('webserver','protocol')
        ip=conf.get('webserver','ip')
        port=conf.get('webserver','port')
        path=conf.get('webserver','path')
        self.url=f'{protocol}://{ip}:{port}/{path}'
    def read_db_conf(self):
        conf=configparser.ConfigParser() # ()不要省略
        conf.read('../conf/db.conf')
        host=conf.get('dbserver','host')
        db=conf.get('dbserver','db')
        user=conf.get('dbserver','user')
        passwd=conf.get('dbserver','passwd')
        self.dbinfo={'host':host, 'db':db, 'user':user, 'passwd':passwd}

if __name__ == '__main__':
    print(Conf().dbinfo,Conf().url)