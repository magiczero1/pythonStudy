'''
a,b=a,2
print(a==a and b==2)
print(a==a and b!=2)
print(a==a or b!=2)

m=[a,2,3,4]
print("a是不是在m里：",a in m)
u="helloworld"
print('e' in u)
'''
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空字典
#以上对象（对象：数据类型）为空或为0的，布尔值都为False.
age = input('请输入你的年龄：')
if age:#如果age不进行判断，那么age的布尔值由输入值决定，当age=0时，执行else，当age！=0时，执行if
    print(age)
else:
    print('您的年龄为',age)

