#!/usr/bin/python3

'''
@File       :  SqliteSingleton.py
@Author     :  LL
@CreateTime :  2019/3/13 22:40
@License    :  
@Desc       :  用于同进程跨服务的数据库操作,多服务多进程时选择使用数据库连接池
'''
import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = DataBase().connect()
db2 = DataBase().connect()
print("DataBase obj1:", db1)
print("DataBase obj2:", db2)
