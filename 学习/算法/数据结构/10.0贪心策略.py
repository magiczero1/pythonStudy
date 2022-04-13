#贪心策略 Greedy Method
#尽可能大，尽可能多
#问题情境：找零钱。

import time

def changeCoin(coinValueList,change,knownResults):  #(硬币兑换体系，目标兑换金额，记录本)
    minCoins = change
    if change in coinValueList:      #递归结束的基本条件
        knownResults[change] = 1     #记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]  #查表成功，返回最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + changeCoin(coinValueList,change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins #找到最优解，并放入记录表中
    return minCoins

coinValueList = [1,5,10]
memo = [0] * 125

print(changeCoin(coinValueList,124,memo))

'''
代码弊端
本质还是暴力使用栈，超出一定数量以后会出现溢出，导致报错。
'''