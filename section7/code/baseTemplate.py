#!/usr/bin/python3

'''
@File       :  baseTemplate.py
@Author     :  LL
@CreateTime :  2020/1/27 22:20
@License    :
@Desc       :  用于基本的命令模型（可以参照windows安装向导）
'''


# Command
class Command:
    def __init__(self):
        pass


# ConcreteCommand
class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv
        print("Build A Command by Receive")

    def execute(self):
        print("Run Command !")


# Invoker
class Invoker:
    def command(self, cmd):
        self.cmd = cmd
        print("Add command to Invoker")

    def execute(self):
        self.cmd.execute()


# Receiver
class Receiver:
    def __init__(self):
        print("Get all Receive Action!")


if (__name__ == '__main__'):
    # 接收到输入信息
    recv = Receiver()
    # 实例化成完整的任务内容包括执行项
    cmd = ConcreteCommand(recv)
    # 调用器实例化
    invoker = Invoker()
    # 在调用器中添加任务
    invoker.command(cmd)
    # 调用器执行所有任务
    invoker.execute()
