#!/usr/bin/python3

'''
@File       :  MetaSingleton.py
@Author     :  LL
@CreateTime :  2019/3/13 22:20
@License    :  
@Desc       :  使用元类来创建单例(单态单例模式)
'''


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Test(metaclass=MetaSingleton):
    pass


print("Test Type :", type(Test))
test1 = Test()
print("Create obj: ", test1)
test2 = Test()
print("Create obj: ", test2)
