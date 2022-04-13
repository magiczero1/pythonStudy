class Person():

    __type = "Human"   #类属性

    def __init__(self,name): #默认实例方法
        self.name = name     #实例属性

    def eat(self):           #实例方法eat
        print(self.name+"敢吃？？")

    @staticmethod
    def sex():               #静态方法sex，与实例对象无关
        return 1

    @classmethod             #类方法，可以访问类里的一切属性，可以用于递归
    def type(cls):
        return cls.__type


    def __str__(self):
        return self.name  #print的默认值

p1 = Person("张三")
print(p1)