class People():
    mailcode=000000
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
    def des(self):
        pass
class Family():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class Student(People,Family):
    def __init__(self,stu_no):
        self.stu_no=stu_no
    def grade():
        pass
class Teacher(People):
    def __init__(self,name):
        self.name=teacher_name

a=People("石头",22,"二仙桥")
print("实例对象a的属性字典：",a.__dict__)
print("People的属性字典：",People.__dict__)
print("a所属的类：",a.__class__)#输出a所属的类
print("Student的父类",Student.__bases__)#输出student所属的父类，输出类型为元组
print("student所属最近的父类:",Student.__base__)#输出student所属最近的父类
print("继承People的子类",People.__subclasses__())#输出继承People的子类，类型为列表
print("Student的族谱：",Student.__mro__)#由近及远输出Student类的族谱