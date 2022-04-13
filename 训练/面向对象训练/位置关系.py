#两个类
#点类（Point）：x,y坐标
#矩形类（Rectangle）：左上角和右下角的坐标

#方法1：计算矩形面积 2：判断点是否在矩形内

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Rectangle():
    def __init__(self,top_left : Point,bottom_right : Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    #定义面积方法
    def square(self):
        length = self.bottom_right[0] - self.top_left[0]
        width = self.top_left[1] - self.bottom_right[1]
        s = abs(length * width)
        return s

    def get_point(self):
        x1 = self.top_left[0]
        x2 = self.bottom_right[0]
        y1 = self.top_left[1]
        y2 = self.bottom_right[1]
        return  x1,x2,y1,y2

    def in_inside(self,p):
        x1 = self.get_point()[0]
        x2 = self.get_point()[1]
        y1 = self.get_point()[2]
        y2 = self.get_point()[3]
        if x1 < p.x < x2 and y1 > p.y > y2:
            return True
        else:
            return False

p1 = Point(3,3)

s1 = Rectangle((2,4),(9,0))
print(s1.square())
print(s1.get_point())
print(s1.in_inside(p1))