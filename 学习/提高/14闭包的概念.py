#多层函数中内部的部分，叫做闭包（抽象）
import time

def outer():
    arg =  10

    def inner():
        nonlocal arg  #声明局部变量为沿用变量
        y = arg + 1

        return y   #注意无法返回y的值

print(outer())

#闭包用于代码运行时间
def runTime(fn,n):

    start = time.time()    #获取当前时间戳
    fn(n)
    end = time.time()

    print(f"{fn}的运行时间为{end - start}")

def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

runTime(fibo,16)