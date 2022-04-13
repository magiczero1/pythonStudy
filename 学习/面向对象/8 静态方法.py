class Person():
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        return (self.name+"正在吃"+food)

    @staticmethod
    def demo():  #静态方法，用途更加广泛，可以不用实例对象的属性，直接调用方法传参
        print("这是一个不需要任何实例对象属性的方法")
        return "---------------------"

    @staticmethod
    def couple(p1,p2):
        return (p1+"和"+p2+"今天成为了夫妻")

p1 = Person("张三")
p2 = Person("李四")

#实例对象调用类方法时，采用的是信息绑定（不直接更改类方法）
print(p1.eat)
print(p2.eat)
#类对象调用类方法，直接是以函数形式调用
print(Person.eat)

#静态方法被类对象和实例对象都可以调用
print(p1.demo())
print(p1.demo)#注意此时没有绑定，是直接调用的函数
print(Person.demo)

print(Person.demo())

#静态方法couple的使用
print(Person.couple("JAck", "Rose"))