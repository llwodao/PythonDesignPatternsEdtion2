#!/usr/bin/python3

'''
@File       :  StockTradeTemplate.py
@Author     :  LL
@CreateTime :  2020/1/28 11:46
@License    :  
@Desc       :  模拟股本交易，但这里只有1个调用者对有限个数Order,并不是实时且连续的，对Order队列也没有回滚和维护操作。
'''


class Order:
    def execute(self):
        print("Run Order!")


class StockTrade:
    def buy(self):
        print("buy some Stocks!")

    def sell(self):
        print("sell some Stocks!")


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)

    def clearAllOrder(self):
        for oneOrder in self.__orderQueue:
            oneOrder.execute()

    def printOut(self):
        print("OrderList: ")
        for oneOrder in self.__orderQueue:
            print(oneOrder)


if (__name__ == '__main__'):
    # Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
    agent.placeOrder(buyStock)
    agent.placeOrder(buyStock)
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
    agent.clearAllOrder()
    agent.printOut()
