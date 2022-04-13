#__eq__
#触发时间：【a】自动触发
#作用：依次调用类对象中的值，并判断是否一致,默认返回值类型为布尔
#参数：self,other
#返回值：True / False
#注意事项：

class Person():
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return "嘿嘿嘿"
        else:
            return

p1 = Person("zhangsan",18)
p2 = Person("zhangsan",18)
print("0x%X"%id(p1))
print(hex(id(p1)),id(p2),sep="\n")
print(p1 is p2)