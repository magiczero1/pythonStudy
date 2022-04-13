#my name is  z  e  r  o
#0123456789  10 11 12 13

a="my name is zero"
print(a[0:20])
print(a[2:])
'''
#使用步长切片[左下标：右下标：步长]
print(a[0:20:3])

del(a)#清空a的值
#从右向左读取[-4：-a] 最小为-a，若切片右侧，则[-5:]
print(a[-4:-a])
'''

list = ["zhangsan","lisi","wangwu","jack","loli"]

for x in enumerate(list):   #针对线性数据可直接返回下标及数据(单个返回元组)
    print(x)

dict = {"name":"zhangsan","age":18,"gender":"male"}   #注意此时返回的仅仅是index和key(两个参数返回对应数据类型的值)
for i,j in enumerate(dict):
    print(type(i),type(j))