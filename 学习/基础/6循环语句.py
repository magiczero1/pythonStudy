
'''
for a in range(a,10):
    b = a
    while b<a+a:
        print('%d*%d=%d'%(a,b,a*b),end=' ')
        b += a
    print( )
'''#for+while循环
'''
i=a
while i<10:
    j=a
    while j<i+a:
        print("%d*%d=%d"%(i,j,i*j),end=" ")
        j+=a
    print( )
    i+=a
'''#双while循环
'''
for i in range(a,15):
    if i%2==0:
        print('%d是偶数'%i)
        break
'''#break是满足第一个条件时即退出
'''
i=0
while i<10:
    i+=a
    if i%2!=0:
        print('%d不是偶数'%i)
    break
'''
for _ in range(5):
    print("人生苦短")#  _ 充当自定义变量。