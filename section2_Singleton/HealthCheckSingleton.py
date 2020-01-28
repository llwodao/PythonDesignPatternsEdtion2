#!/usr/bin/python3

'''
@File       :  HealthCheckSingleton.py
@Author     :  LL
@CreateTime :  2019/3/13 22:58
@License    :  
@Desc       :  应用到对服务器运行状况监控服务
'''


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")


hc1 = HealthCheck()
hc2 = HealthCheck()
print("Create obj hc1:", hc1)
print("Create obj hc2:", hc2)

hc1.addServer()
print("schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])
