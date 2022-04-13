#调用自身的函数，必须具有结束条件

def digui():
    print("递归开始")
    digui()

#digui()   #没有结束条件会栈溢出

def getSum(n:int):
    if n == 1:                #停止条件
        return 1
    else:
        return n+getSum(n-1)  #注意调用自身必须向停止条件靠拢

print(getSum(10))

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)  #两个都要向停止条件靠拢


print(fibo(9))