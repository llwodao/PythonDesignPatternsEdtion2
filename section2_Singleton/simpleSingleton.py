#!/usr/bin/python3

'''
@File       :  simpleSingleton.py
@Author     :  LL
@CreateTime :  2019/2/20 0:31
@License    :  
@Desc       :  用重载__new__的方式实现实例化
'''


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.num = 0


'''Tip 
cls is class_self
cls和self类似,但用于类方法调用,和实例无关。
'''
s = Singleton()
b = Singleton()
print("Created :", s)
print("Created :", b)

'''Tip
Singleton means use a class mem in many instance
一个类和其内存可以被不同的对象使用和共享。
is that thread safe?
是否线程安全呢？
the turth is not all 
并非所有都能

'''
s.num = 10
print("Num :", s.num)
print("Num :", b.num)
b.num = 12
print("Num :", s.num)
print("Num :", b.num)
