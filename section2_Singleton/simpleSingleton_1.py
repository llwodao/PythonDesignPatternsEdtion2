#!/usr/bin/python3

'''
@File       :  simpleSingleton_1.py
@Author     :  LL
@CreateTime :  2019/2/25 22:43
@License    :  
@Desc       :  懒汉式实例化
'''


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance is already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


class MyTest:
    def __init__(self):
        print("__init__")

    @classmethod
    def test(self):
        self.s = MyTest()
        print(self.s)


# init 只是初始化，真正创建是通过__new__
t1 = MyTest()
print(t1)
t1.test()

# 初始化类的地方
s = Singleton()
# 创建实例对象的地方
print("Object Created", Singleton.getInstance())
# s1 = Singleton()
