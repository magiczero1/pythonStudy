#python支持多继承,其他语言不一定支持

class Plant():
    def a(self):
        print("崽子，我是一棵植物")

    def life(self):
        print("植物的生命有500年")

class Person():
    def b(self):
        print("我是一个人")

    def life(self):
        print("人的生命只有100年不到")

class C(Plant,Person):

    def c(self):
        print("别吧，我不想当植物人``````")


p1 = C()
p1.a()
p1.b()
p1.c()
p1.life()  #默认按照继承顺序进行调用，继承顺序决定了广度还是深度。可以使用 类名.__mro__ 查看继承顺序
print(C.__mro__)