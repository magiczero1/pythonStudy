#封装 保证程序安全（若不希望该类属性被外部所使用，则加__）
class Car():
    def __init__(self,brand,type):
        self.brand=brand
        self.__type=type#不希望被外部访问
    def start(self):
        print("启动了")
brand1=Car("奔驰","s300")
print(brand1.brand)
try:
    print(brand1.__type)#type被隐藏
except:
    print(brand1.__dir__(),end="\n")
    print(brand1._Car__type)#强制访问类属性
#继承  默认继承object父类
#父类
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名：{0},年龄：{1}'.format(self.name,self.age))
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)#利用super()去调用父类中的实例属性,
        self.score=score

class Teacher(Person):
    def __init__(self,name,age,teachyear):
        super().__init__(name,age)
        self.teachyear=teachyear
    def info(self):
        super(Teacher, self).info()
        print("教龄",self.teachyear)

stu1=Student("罗翔",20,99)
tea1=Teacher("张三",43,28)
stu1.info()
tea1.info()
#多态
#类的组成   在类之外称为函数，类之内称为方法
'''
class Student:#Student为类名，由一个或者多个单词组成，每个单词的首字母大写。
    native_place='吉林'#类属性，直接写在类中的变量即为类属性
    def __init__(self,name,age):#name,age 为实例属性，__init__是初始化空间
        self.name=name
        self.age=age
    def info(self):  #实例方法
        print('我的名字叫',self.name,'年龄是',self.age,'岁')
    #类方法
    @classmethod
    def cm(cls):
        print("类方法")
    #静态方法，不允许使用self
    @staticmethod
    def sm():
        print('静态方法')
#创建Student类的对象
stu1=Student("张三",18)
stu1.info()          #第一种调用方法   实例名.方法名
Student.info(stu1)   #第二种调用方法   类名.方法名(实例对象）

#类属性的使用方法
print(Student.native_place)
stu2=Student("李白",289)
stu3=Student("韩信",689)
stu3.native_place='上海'
print(stu3.native_place)

#类的动态绑定属性,直接创建空间及实例属性
stu3.gender="男"
#类的动态绑定方法,直接创建类方法
def show():
    print("aaaa")
stu2.show=show#绑定方法不用加（）
stu2.show()#动态绑定后，直接调用
'''