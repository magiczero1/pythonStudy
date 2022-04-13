#第一种写法，全部导入
import math as M#如果自定义了模块名称，原模块名失效
import turtle
print(M.modf(111))
print(dir(M))#遍历模块中的指令集
#第二种写法，全部导入
from math import *
from turtle import forward #部分导入，有效降低内存

import demo_package.module1 as age#从包里导入模块
import demo_package.module2 as name
age1=age.age
name2=name.name
print("我的名字叫{1},今年{0}岁了".format(age1,name2))