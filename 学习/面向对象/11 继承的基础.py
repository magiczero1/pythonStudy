class Animal():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name+"昏睡百年")


class Dog(Animal):

    def bark(self):
        print(self.name+"要咬人哦")


class Student(Animal):

    def study(self):
        print(self.name+"今天不学习，明天变垃圾")


jiwawa = Dog("吉娃娃",3)

student1 = Student("张三",18)

jiwawa.sleep() #会自动找父类的方法
jiwawa.bark()

student1.sleep()
student1.study()