#可变类型的传参  如列表、字典等
def test2(num):
    num[0] = 999

list = [1,2,3,4,5]
test2(list)
print(list)    #数据发生改变

#不可变类型的传参  如纯数字、元组等
def test1(a):
    a = 100

x = 10
test1(x)
print(x)      #数据没有发生改变


#参数为函数
def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def calc(a,b,fn):
    x = fn(a,b)
    return x

print(calc(100,20,minus))   #非常实用