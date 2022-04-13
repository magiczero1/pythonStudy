#单例就是调用同一个地址，不会生成其他空间

class Single():
    __instance = None #定义调用状态
    __isfirst = True #定义是否第一次的数据

    def __new__(cls, *args, **kwargs):  #单例重写new方法
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  #申请内存空间
        return cls.__instance

    def __init__(self,a):
        if self.__isfirst == True :
            self.a = a
            self.__isfirst = False  #为实例对象创建了新的私有属性，但是也可以用于状态判断



p1 = Single("哈哈")
p2 = Single("嘿嘿")
print(p1 is p2)
print(p1.a)
print(p2.a)