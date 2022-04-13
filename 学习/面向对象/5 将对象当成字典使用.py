class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        self.__dict__[key] = value

p1 = Person("张三",18)
p1.__dict__["name"] = "李四"
print(p1.__dict__["name"])

#使用__setitem__方法后，可以直接把对象当成字典使用
p1["age"] = 99 #可以被修改，但是不能被输出
print(p1.name)
print(p1.age)