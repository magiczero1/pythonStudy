#注释一行
#变量
a=1
#函数
#print('AWM')
'''
num1=input("输入第一个数字：")#str字符串类型
num2=input("输入第二个数字：")
c=float(num1)*float(num2)    #float()浮点数   int()整数
print(c)
'''#input()函数
#eval() 只适用于+  -
'''
x=18
y=5
z=eval("x-y")
print(z)
'''
'''
num1=input("输入要数的数字：")#str字符串类型
num2=input("1s数几个：")
min=60
hour=60
c=float(num1)/float(num2)    #float()浮点数   int()整数
print('要数的秒数：',c)
min=c/60
print('要数的分钟数：',min)
hour=min/60
print('要数的小时数：',hour)
day=hour/24
print('要数的天数：',day)
'''
#数据类型
'''
str()#字符串
int()#整数
float()#浮点数
'''
#ascii码
#print("a的ascii码是：",ord("a"))
#print("ascii码是1的字符是：",chr(a))
import random
for i in range(5):
    print(random.randint(3,8))


