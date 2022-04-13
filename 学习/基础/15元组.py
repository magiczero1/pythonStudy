#可变序列对象  列表、字典 【id保持一致即可进行增删改】
#不可变序列对象  元组、字符串 【增删改都会使得id不一致】
'''
a=[a,2,3]
print('原来的id',id(a))
a.append(6)
print('增加元素后的id',id(a))

b=('张三','李四','王五')
print('原来的id',id(b))
b=('张三','李四','王五','赵六')
print('增加元素后的id',id(b))
'''
#元组() 元组也可以用索引
'''
t1=(a,2)#第一种写法
t2=tuple((a,2))#第二种写法,注意有两个（）
print(t1)
print(t2)
k=()#空元组
print(k)
'''
#元组中内嵌套列表，及遍历
b=['盖伦','剑魔']
a=('阿卡丽',b,'疾风之心')
for i in range(3):
    print(a[i],id(a[i]))
print('——'*12)
b.append('洛手')
for i in range(3):
    print(b[i],id(a[i]))