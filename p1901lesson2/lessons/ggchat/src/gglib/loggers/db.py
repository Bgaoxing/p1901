# 设置日志存储地址
from abc import ABC

from gglib.logger import BaseLogger
import pymysql


class MySQLLogger(BaseLogger):
    def __init__(self, level, fmt, host, port, user, password, db):
        super().__init__(level, fmt)
        self.mysql_connection = pymysql.connect(host=host,
                                                port=port,
                                                user=user,
                                                password=password,
                                                database=db)

    def debug(self, sender, *args):
        assert isinstance(self.mysql_connection, pymysql.Connection)
        pass
