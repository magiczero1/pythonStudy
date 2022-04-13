import time
def sum0fN(n): #第一种迭代算法
    start = time.time()
    sum = 0
    for i in range(1,n+1):
        sum += i
    end = time.time()
    return sum,end - start

def sum0fN1(n):#第二种高斯算法
    start = time.time()
    sum = 0
    sum = (1+n)*n/2
    end = time.time()
    return sum, end - start

if __name__ == '__main__':
    for i in range(5):
        print("结果是%d，需要%10.7f 秒"%sum0fN(1000000))
    print("-----------------")
    for i in range(5):
        print("结果是%d，需要%10.7f 秒"%sum0fN1(1000000))
