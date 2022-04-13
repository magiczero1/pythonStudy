
def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)   #数列前两项和

print(fibo(19))  #只能返回最终结果

for i in range(1,100):  #利用for循环输出要求的整个数列
    print(fibo(i))