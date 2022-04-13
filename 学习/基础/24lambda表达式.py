import random

#第一种用法，定义匿名函数(简化函数代码)
add = lambda x,y:x+y
print(add(3,4))

#第二种用法，三项表达式(匿名函数的拓展)
value = lambda x: "偶数" if x%2 == 0 else "奇数"
print(value(10))

#第三种用法，无参数表达式
a = lambda: random.random()
print(a())          #注意必须加()否则返回的是对象

#第四种，与map()函数联用
mobj = map(lambda x:x**2,[1,2,3,4])  #依次取数并放进前者进行计算
for i in mobj:
    print(i)