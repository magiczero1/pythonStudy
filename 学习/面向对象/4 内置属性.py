class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        return self.name+"吔屎啦"

p1 = Person("张三",19)
print(p1.eat())

print(dir(Person))#查看Person的所有方法