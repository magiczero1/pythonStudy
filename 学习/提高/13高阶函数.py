#一个函数作为另一个函数的返回值
def add(x,y):
    sum = x+y
    minus = x-y
    return mutl(sum,minus)

def mutl(a,b):
    result = a*b
    return result

print(add(100,99))


#一个函数作为另一个函数的参数
def year(num):
    if num%100==0 and num%400==0:
        return True
    elif num%100!=0 and num%4==0:
        return True
    else:
        return False

def output(num):
    if year(num):
        print(f"{num}是闰年")
    else:
        print(f"{num}是平年")

print(output(1997))


#函数内部再定义一个函数

def range1(num):

    def range2(num):
        if num%2 == 0:
            return True
    if range2(num):
        return f"{num}是偶数"
    else:
        return f"{num}是奇数"

print(range1(19))