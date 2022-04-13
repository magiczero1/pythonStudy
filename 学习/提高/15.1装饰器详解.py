#装饰器可对不同的函数进行装饰
import time

def runTime(fn):
    def runtime_innner():
        start = time.time()
        fn()
        end = time.time()
        print("程序执行用时{:.5f}".format(end - start))
    return runtime_innner


@runTime
def fractorial():
    n = 1000
    if n < 2:
        return n
    else:
        res = 2 ** n
    return res

@runTime
def Sums():
    n = 1000
    if n < 2:
        return n
    else:
        return n**2

Sums()
fractorial()  #此时结果返回的是装饰器结果，而非函数本身



@Sums
def test1():
    pass

test1()#注意报错类型

