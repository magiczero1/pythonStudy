#如果不加以限制，则类对象本身具有动态属性。
#因此使用__slots__方法进行限制
class Student(object):
    __slots__ = ("name","age")  #限制类属性仅有name和age
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"大家好，我是{self.name}")

s1 = Student("Jack",19)
s1.height = "180cm" #此时已经报错，与2中进行对比
print(s1.height)