#*args 可变位置参数
def say(a,b,*args):
    print(f"a={a},b={b}")
    print(*args)     #以元组的形式保存剩余参数

say(1,2,3,4) #可传多个，但不输出

#形参、可变参、缺省参位置必须相对存在
def math(a,b,*args,mutl = 5):
    print((a+b)*mutl)

#注意以下的区别
math(1,2)
math(1,2,100)   #100以元组形式保存在args里
math(1,2,mutl=100)

#**kwargs  可变关键字参数
def math2(a,b,*args,mutl = 5,**kwargs):
    print((a + b) * mutl)
    print(kwargs)

math2(1,2,mutl=100,minus=1)  #minus=1以字典形式保存在kwargs中
