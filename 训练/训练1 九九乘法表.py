#九九乘法表1
'''
i=a
while i<10:
    j=a
    while j<i+a:
        print(i,'*',j,'=',i*j,end=" ")
        j+=a
    print(" ")#换行符
    i+=a
'''
#九九乘法表2
'''
a=9
while a<10 and a>=a:
    b=9
    while b>a-a:
        print(a,'*',b,'=',a*b,end="|")
        b-=a
    print(" ")
    a-=a
'''
#九九乘法表3
'''
a=9
while a<10 and a>=a:
    for b in range(a,10):
        if a>=b:
            print(a,'*',b,'=',a*b,end="|")
    a -= a
    print(" ")
'''
#输出1-100水仙花数153=a*a*a+5*5*5+3*3*3
'''
for a in range(a,1000):
    b=a//100# 对a进行100取整，留下百位
    c=a%10#对a取余，留下个位
    d1=(a-b*100-c)//10  #第一种写法对d取整，留下十位
    d2=a//10%10         #第二种写法对a除10取整，留下前两位，然后取余留下十位
    if a==b**3+c**3+d2**3 and a>=100:
        print(a,'是水仙花数')
'''
#输出5的倍数
#第一种写法，直接输出
for a in range(1,51):
    if a%5==0:
        print('a=',a,'是5的倍数')
#第二种写法，使用continue，反向输出
for b in range(1,51):
    if b%5!=0:
        continue
    print('b=',b,"是5的倍数")


