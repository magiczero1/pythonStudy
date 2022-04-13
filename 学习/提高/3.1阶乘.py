#双函数求阶乘和  1!+2!+3!+``````

#求阶乘函数
def factorial(m):
    if m == 1:
        return m
    else:
        return m*factorial(m-1)

def sumFac(m):
    sum = 0
    for i in range(1,m+1):
        sum += factorial(i)
    return sum

print(sumFac(10))