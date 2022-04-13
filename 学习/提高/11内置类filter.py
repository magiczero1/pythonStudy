from functools import reduce
#filter  过滤器
list1 = [199,299,399,499]
result = filter(lambda arg:arg>199,list1)   #返回可迭代对象，利用for循环或者数组进行输出

#利用数组进行输出
print(list(result))
'''！！！注意，迭代器仅限于使用一次，下面的无法正常输出！！！'''
#for循环输出
for i in result:
    print(i)

#map    依次按要求操作,返回可迭代对象
list2 = [1,2,3,4,5,6]

def division(num):
    return num/5

x = map(lambda arg:division(arg),list2)  #可以使用函数进行操作

print(list(x))


#reduce   依次取数求满足某种条件的算式，有点像递归.返回一个数值

def add(x,y):
    return x+y

list3 = [1,1,2,3,5,8,13]

x = reduce(add,list3)
print(x)

y = reduce(lambda x,y:x-y,list3)
print(y)
