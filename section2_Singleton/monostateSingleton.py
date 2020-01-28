#!/usr/bin/python3

'''
@File       :  monostateSingleton.py
@Author     :  LL
@CreateTime :  2019/3/2 20:00
@License    :  
@Desc       :  单态模式（可以有不同对象，但是共享的状态是相同的）
'''


class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        print("My id:", id(self.__dict__))
        # self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
b.g = "hello"
# 测试发现，当赋值操作时，python会直接指向值的地址，这样即可减少赋值所需的拷贝时间。
a = 0
print("a.id: ", id(a))
c = 1
print("c.id: ", id(c))
a = c
print("a.id: ", id(a))
b.x = 4
print("Create Brog b: ", b)
print("Create Brog b1: ", b1)
# __dict__用于存放class里的成员参数,设置共享后，等同于不同对象的参数都共享了一个内存空间
print("b.__dict__: ", b.__dict__, id(b.__dict__))
print("b1.__dict__: ", b1.__dict__, id(b1.__dict__))
# 其实borg类就是一个工厂对象
print("Borg.__dict__: ", id(Borg.__dict__))
