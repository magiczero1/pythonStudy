# 利用@对函数进行修饰，接闭包。
import time,math


def sayRunTime(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时{}".format(end-start))

    return inner

@sayRunTime   #首先调用装饰函数sayRuntime，然后将被装饰的函数Sqrt传上去(此时inner函数还没有被调用)
def Sqrt():
    res = 1000000000**0.5
    return res

Sqrt()  #实例化时才调用inner，且返回值是inner