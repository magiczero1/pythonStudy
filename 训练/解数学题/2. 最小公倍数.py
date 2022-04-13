#最小公倍数怎么算
'''
x = int(input("请输入第一个数字："))
y = int(input("请输入第二个数字："))
if x%y==0:
    x,y=y,x
    print(y,"是{0}和{1}的最小公倍数".format(x,y))
else:
    for i in range(x,x*y+1):
        if i%x==0 and i%y==0:
            print(i,"是{0}和{1}的最小公倍数".format(x,y))
            break
'''
#最大公约数怎么算
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
if a>b:
    i = a-1
    while i > 1:
        if a%i==0 and b%i==0:
            print(i,"是{0}和{1}的最大公约数".format(a,b))
            break
        i-=1
else:
    a,b=b,a
    i = a - 1
    while i > 1:
        if a%i==0 and b%i==0:
            print(i,"是{0}和{1}的最大公约数".format(a,b))
            break
        i -= 1