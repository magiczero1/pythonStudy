from timeit import Timer
#移除末尾
popend = Timer("x.pop()","from __main__ import x")
popzero = Timer("x.pop(0)","from __main__ import x")
popmid = Timer("x.pop(len(x)//2)","from __main__ import x")
'''
print(popend.timeit(1000))
print(popzero.timeit(1000))
'''
#展示增长趋势
for i in range(10000,100001,10000):
    x = list(range(i))              #设定传参x，随机生成数
    pe = popend.timeit(1000)        #1000次pop()运算的时间
    pz = popzero.timeit(1000)       #1000次pop(0)运算的时间
    pm = popmid.timeit(1000)
    print ("pe%7.5f,pz%7.5f,pm%7.5f" %(pe,pz,pm))
