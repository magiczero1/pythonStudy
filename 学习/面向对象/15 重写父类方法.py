class Person():
    def __init__(self,name):
        self.name = name

    @staticmethod
    def sleep():
        print("我要睡觉了")


class Student(Person):
    #第一种实例属性的继承方法，利用父类名.方法名(继承属性)
    def __init__(self,school):
        Person.__init__(self,name)
        self.school = school

    # 重名，直接修改方法
    @staticmethod
    def sleep():
        print("学生不能上课睡觉")

class Doctor(Person):
    #利用super(子类名,self).方法名(属性名)，直接调用父类的方法及属性
    def __init__(self,name,salary):
        super(Doctor, self).__init__(name)
        self.salary = salary
