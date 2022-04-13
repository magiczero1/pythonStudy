#模块就是一个py文件
import time  #直接导入
from random import randint #导入方法,可直接使用
from math import *  #导入全部方法和变量，不推荐使用
import datetime as dt  #别名导入模块
from copy import deepcopy as dp  #别名导入方法

print(time.time())  #获取时间戳
print(randint(0,2))
print(e)  #math里的内置变量
print(dt.MAXYEAR)