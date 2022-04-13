#__add__对象相加,无论对象是文本或者数据，都可以拼接操作
'''
a=20
b=30
c=a+b
print(c)
d=a.__add__(b)#底层对象操作逻辑
print(d)

fname="张"
lname="无忌"
full_name1=fname+lname
print(full_name1)
full_name2=fname.__add__(lname)
print(full_name2)
'''
#自定义类的add操作
class Weather:
    def __init__(self,weather):
        self.weather=weather
    def __add__(self, other):    #如果想要类中的实例属性进行合并操作，就必须要写该方法
        add=self.weather+other.weather
        return add
    def __len__(self):
        return len(self.weather)
weather1=Weather("晴天")
weather2=Weather("阴天")
s=weather1.__add__(weather2)
print(s)
#__len__读取实例对象的字符长度,若类中没写，则无法调用该方法
print(len(weather2))
print(s.__len__())
#__new__ 创建对象

#__init__初始化对象
