#无参装饰器
import time

def runTime(fn):
    def runtime_innner():
        start = time.time()
        res = fn()
        end = time.time()
        print("程序执行用时{:.5f}".format(end - start))
        return f"原来函数的结果是：{res}"
    return runtime_innner

@runTime
def test1():
    x = 0
    for i in range(10000):
        x += 1
    return x

test1()  #此时返回的是runtime_inner的执行结果，即print

print(test1())   #输出了两条,第一条是自带的print，第二条是test1()的结果