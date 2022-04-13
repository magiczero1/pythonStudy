#倒序索引  -7 -6 -5 -4 -3 -2 -a
#          A  B  C  D  E  F  G     列表可以存储不同数据类型。如A："你好"  B:12.3  C:True
#顺序索引   0  a  2  3  4  5  6     一个列表中拥有0个以上的对象
'''
s=['hello','world','python',a]
if 'hello' in s:
    print(s[0:2])
'''
#列表的写法
'''
m=['hello','world','python',a] #直接将所有对象存储在列表s中
n=list(['hello','world','python',2])#将对象存储在list中，然后赋值给s
print(m[-a])
print(m[3])
'''
#列表中对象的索引获取方式 利用index  注意，如果同时存在相同的对象，则只显示第一个
'''
m=['hello','world','python',a,'hello']
print(m.index('hello'))
'''
#列表的切片
'''
m=['hello','world','python',a,'hello']
print('a',m[::2])#按步长为2切片
print('2',m[:2])#从索引0开始，切到索引2
print('3',m[a::2])#从索引1，步长为2
print('4',m[::-a])#逆序输出
print('5',m[::-2])#逆序输出
print('6',m[a::-a])#从索引为1，逆序输出
'''
#操作列表中的对象
#append 末尾增加1个元素，该对象可以是单元素，也可以是列表
'''
s1=[a,2,3,4,5]
s2=[a,2,3,4,5]
s1.append(6)
print('增加了元素',s1)
s1.append(s2)
print('增加了元素',s1)
'''
#insert列表的指定位置增加一个对象,该对象可以是单元素，也可以是列表
'''
s1=[a,2,3,4,5]
s2=[a,2,3,4,5]
s1.insert(2,9) #若位置大于索引，则在末尾插入,自动删除空行
print(len(s1))
print(s1)
s1.insert(2,s2)
print(s1)
'''
#extend末尾增加元素,等同于合并列表
'''
s1=[a,2,3,4,5]
s2=[a,2,3,4,5]
s1.extend(s2)
print(s1)
s1.extend(7)#注意这个位置！加进去会自动出现''
print(s1)
'''
#切片插入    从任意位置合并两个列表(会覆盖后面的）
'''
s1=[a,2,3,4,5]
s2=[a,2,3,4,5]
s1[a:]=s2
print(s1)
s1[-a:]=s2
print(s1)
'''
#remove删除列表中的首个符合条件的元素
'''
s1=[a,2,3,4,5,a]
s2=[a,2,3,4,5]
s1.remove(a)
print(s1)
'''
#pop删除列表中指定索引的元素
'''
s1=[a,2,3,4,5,a]
s2=[a,2,3,4,5]
s1.pop(0)
print(s1)
s1.pop()#默认移除列表中的最后一个元素
print(s1)
'''
#切片删除 按索引批量删除
'''
s1=[a,2,3,4,5,a]
s1[a:3]=[]
print(s1)
'''
#clear 清空列表中的所有元素
'''
s1=[a,2,3,4,5,a]
s1.clear()
print(s1)
'''
#del 摧毁整个列表
'''
s1=[a,2,3,4,5,a]
del s1
print(s1)
'''
#利用下标进行 元素替换 注意，若对切片进行替换，赋值一定是数组
'''
s1=[a,2,3,4,5,a]
s1[a]=10
print(s1)
s1=[a,2,3,4,5,a]
s1[a:4]=[6,7,8,9]
print(s1)
'''
#列表生成式
s=[i for i in range(2,11,2)]
print(s)
s=[i*2 for i in range(1,6)]
print(s)