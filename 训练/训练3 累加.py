#简单累加
'''
a=0
sum=0#一定对sum赋值
while a<5:
    sum+=a
    a += a
print(sum)
'''
#步长累加
'''
sum=0
for i in range(a,101):
    if i%2==0:
        sum+=i
print(sum)#输出最终结果

sum=0
for i in range(a,101):
    if i%2==0:
        sum+=i
    print(sum)#执行一次输出一次
'''
i = 0
sum = 0
while i<101:
    if i%2==0:
        sum+=i
    i+=1
print(sum)