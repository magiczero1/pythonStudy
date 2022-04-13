class Person():
    def __init__(self,name):
        self.name = name

    def eat(self,food): #实例方法
        return self.name+"正在吃"+food

    @classmethod  #最多会用到类属性，一般不使用实例属性和实例方法
    def test1(cls):  #test1 可以拿到Person里的eat方法，但是已经无法拿到self.name
        pass

    @staticmethod
    def couple(a,b):
        return f"恭喜{a}、{b}喜结良缘"


print(Person.couple("张三", "李四"))
p1 = Person("张安")
print(p1.test1)