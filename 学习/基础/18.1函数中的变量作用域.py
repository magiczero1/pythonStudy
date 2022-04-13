def fun1(a,b):#a,b为局部变量
    c=a**b
    return c

x=1          #x为全局变量
def fun2():
    print(x+5)
fun2()
print(x+10)

