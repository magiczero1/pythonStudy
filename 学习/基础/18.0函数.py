'''
def calc(a,b):                #a,b叫做形参
    c=a+b
    print(c)
    return c
calc(9,10)                    #9，10实参
calc(b=92,a=13)
'''
'''
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2==a:
            odd.append(i)
        else:
            even.append(i)
    return odd,even   #返回值是一个元组
lst=[3201,1120,121,12,3,31,a,2223,14]
print(fun(lst))
'''
#1函数返回值的区别
'''
def fun1(a,b):
    c=a/b
    return c#结果返回给c输出0.a，不返回则输出none
result1=fun1(10,100)
print(result1)
'''
#2函数默认值
'''
def fun2(x=0.99,y=2):
    z=x**y
    return z
result2=fun2()#若实参部分不填写，则调用默认值。
print(result2)
result3=fun2(8,3)#若实参部分填写，则调用实参值。
print(result3)
'''
#3*定义个数可变的位置形参，返回类型为元组
def fun3(*a):
    print(a)
fun3(10,222,11231)#不需要变量可直接返回元组类型的值
lst3=[120,121,12223345]
fun3(lst3)#作为整个列表，返回元组
fun3(*lst3)#列表中的每个值返回元组
#3**定义个数可变的关键字形参，返回值为字典
def fun4(**y):
    print(y)
fun4(a=10,b=20,c=111,d=1231)#必须要变量，返回类型为字典的值
dic4={"q":223,"w":131,"e":655,"r":12}
'''fun4(dic4)#报错'''
fun4(**dic4)

'''函数定义时的顺序'''
def fun1(a,b,*,c,d):   #*之后的c，d只能以关键字c=11，d=22实参传递，而a，b不影响
    pass
def fun2(*args,**args2):#参见上面
    pass
def fun3(a,b=10,*args,**args2):
    pass