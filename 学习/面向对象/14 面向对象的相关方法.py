class Person():
    def __init__(self,name):
        self.name = name

class Student(Person):
    pass

p1 = Person("张三")
p2 = Person("张三")

#使用is判断对象是否是同一个(指向的地址是否一样)
print("OX%x" %id(p1))
print("OX%x" %id(p2))
print(p1 is p2)

#使用isinstance(a,(A,B))判断a是否含有A,B的基因
s1 = Student("李四")


print(isinstance(s1,(Person,Student)))

print(isinstance(s1, Student))

print(isinstance(s1, Person))

#使用issubclass(A,B)判断A是否是B的子类
print(issubclass(Student, Person))