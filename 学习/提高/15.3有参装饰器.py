#有参装饰器，注意参数出现的位置！
import time

#单参装饰器
def runTime(fn):
    def runtime_innner(*args,**kwargs):
        start = time.time()
        res = fn(*args)
        end = time.time()
        print("程序执行用时{:.5f}".format(end - start))
        return f"原来函数的结果是：{fn,res}"
    return runtime_innner

@runTime
def test2(m):
    x = 0
    for i in range(m):
        x += 1
    return x

test2(1000000)  #此时返回的是runtime_inner的执行结果，即print

print(test2(1000000))


#多参装饰器  需要对inner函数附加可变参