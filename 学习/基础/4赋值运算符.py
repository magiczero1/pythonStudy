a=b=c=2  #链式赋值
print(a,b,c)

d,e=4,6 #解包赋值

d,e=e,d #赋值交换
print(e,d)

a=1.1231
b=1.1231  #单独的数，id = id ，value = value
print(id(a))
print(id(b))
print(a is b)

m=[1,2,3,4]
n=[1,2,3,4]
print(type(m))
print(m == n)
print(m is n)