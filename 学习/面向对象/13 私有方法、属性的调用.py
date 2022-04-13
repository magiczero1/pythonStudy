#私有方法一般无法被继承，但可以被访问

class Animal():
    __tail = "大部分动物都有尾巴"

    def __wise(self):
        print("很少有动物有高级智慧")
        return 0


class Person(Animal):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


p1 = Person("张三")
print(p1)

#通过实例名._父类名__方法/属性名即可调用，一般不建议使用

print(p1._Animal__tail)

print(p1._Animal__wise())  #注意此时无返回值