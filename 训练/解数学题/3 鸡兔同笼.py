# x 头的个数
# y jio的条数
x = int(input("请输入头有几个："))
y = int(input("请输入jio有几条："))
'''
for a in range(x+1):  # a 有几只🐔
    b = x - a            # b 有几只兔
    if 2*a+4*b==y:
        print(a,b)
'''
b = y/2 - x  #腿减去一半，减去头的个数，剩下的就是兔子的只数
a = x - b    #总头数减去兔子的只数，剩下的就是鸡的只数
print(a,b)

