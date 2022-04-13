#多态：通过子类，重写父类的方法。      龙生九子，各有不同

#场景  日常生活中，根据狗的作用，可以分为导盲、缉毒犬、田园犬等，一个人的职业不确定时，与其合作的狗伙伴也不确定。
#针对上述场景，实现多态的操作

class Dog():

    def work(self):
        print("修勾开始工作")



#以下是Dog的子类
class BlindDog(Dog):
    def work(self):
        print("导盲修勾正在导盲中~~~~~~")

class PoliceDog(Dog):
    def work(self):
        print("警修勾要去巡逻了``````")

class EarthDog(Dog):
    def work(self):
        print("马丹，高贵的中华田园修勾被拴在家了凸(艹皿艹 )")


#人类
class Person():
    def __init__(self,name):
        self.name = name

    def work_with_dog(self):
        print("开始工作咯:",end = "")
        self.dog.work()    #注意self.dog 必须实例化，否则会出问题


pd =PoliceDog()
bd = BlindDog()
p1 = Person("张三")

p1.dog = EarthDog()
p1.work_with_dog()