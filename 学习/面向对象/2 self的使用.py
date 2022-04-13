class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"大家好，我是{self.name}")
s1 = Student("Jack",19)
print(s1.name)
print(Student("Rose", 20).name)
s1.sayHello()
#Student("Jack",19)这段代码的执行过程
#1.调用__new__方法，开辟一段内存空间
#2.调用__init__方法，将参数传入，并以self指向创建好的空间并赋值    其实self指的就是Student类本身
#3. s1.name与下面的方法一样

#添加类属性（类似于字典）
s1.height = "170cm"  #动态属性
print(s1.height)
