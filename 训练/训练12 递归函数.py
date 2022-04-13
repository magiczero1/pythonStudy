def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)#注意这里和循环不一样的是不能使用 n=n*(n-a)##阶乘
print(fac(6))#阶乘

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        res=fib(n-1)+fib(n-2)
        return res#阶乘
print(fib(6))#斐波那契
for i in range(1,30):
    print(fib(i))

