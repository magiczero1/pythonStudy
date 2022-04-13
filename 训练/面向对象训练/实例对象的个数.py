class Person():
    __count = 0
    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        x = object.__new__(cls) #申请内存
        return x

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def class_obj_count(cls):
        return cls.__count

p1 = Person("jack",16)
p2 = Person("KK",99)
p3 = Person("沙丽",23)
p4 = Person("沙",23)

print(Person.class_obj_count())