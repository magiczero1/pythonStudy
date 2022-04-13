class Student():
    #__init__方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    #行为定义为一个个函数
    def run(self):
        print(f"{self.name}跑步中")

    def eat(self):
        print(f"{self.name}吃饭中")

#实例化对象,一定要与属性对应（例如scratch中的方向、大小等）
s1 = Student("张三",14,"175cm")
s1.run()