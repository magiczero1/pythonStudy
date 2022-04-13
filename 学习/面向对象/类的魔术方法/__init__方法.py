#__init__初始化*****
#触发时间：实例化后触发
#作用：为对象添加所属成员
#参数：self用于接收所有对象，其他参数根据实例化的传参决定
#返回值：无
#注意事项：无
class Human:
    def __init__(self,name,age,sex):#此处形参用来接受实例化时的对象
        print(self)
        self.sex = sex
        self.age = age
        self.name = name
    def eat(self):
        print("吃饭方法")
    def sleep(self):
        print("睡觉方法")
    def sport(self):
        print("运动方法")
one=Human("刘佳怡",1,"女")#此处叫做实例化，【a】制作一个对象【2】为对象初始化操作
print(one)
print(one.__dict__)