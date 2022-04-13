#学生类Student
#属性：学号、姓名、年龄、性别、成绩

#班级类Grade
#属性：班级名称、班级中的学生[列表存储]
#方法：①查看该班所有学生信息 ②查看指定学号的学生信息 ③查看班级成绩不及格的学生信息 ④将班级中的学生按照成绩降序排列

class Student():
    def __init__(self,id,name,age,sex,score):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def __str__(self):
        return f"{self.id,self.name,self.age,self.sex,self.score}"

class Grade():
    def __init__(self,class_name,studentlist=None):
        self.class_name = class_name
        if studentlist is None:
            studentlist = []
        self.studentlist = studentlist

    def show_all(self):
        return f"{self.studentlist}"

    def show_student(self,id):
        pass

    def fail_student(self):
        pass

    def scores_do(self):
        pass