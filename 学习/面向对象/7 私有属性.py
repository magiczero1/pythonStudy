class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__salary = 1000000000  #私有属性，外部不容易访问

    def salary_up(self):
        self.__salary += 10

    def get_salary(self):
        #可以记录访问数据的一些细节
        return self.__salary

    def set_salary(self,num):
        print("工资被修改了")
        self.__salary = num

    def __inner(self):  #私有方法
        if self.name == "张三":
            self.name = "【法外狂徒】·"+self.name

p1 = Person("zhangsang",18)

#获取私有变量的方式
#① _类名__私有属性名
print(p1._Person__salary)

#②接口：定义get 和 set 的方法去获取、修改
print(p1.get_salary())