#点类：x,y坐标
#圆类：圆心center_point，半径radius
#方法：圆面积、周长、圆与点的位置关系：内、外、上
import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class Circle():
    def __init__(self,center_point,radius):
        self.center_point = center_point
        self.radius = radius    #半径

    def suqare(self):
        return "%.2f"%(3.14*self.radius*self.radius)

    def perimeter(self):   #周长
        return "%.2f"%(3.14*2*self.radius)

    def position_with_point(self,point):
        #使用try......except处理可能出现的数据类型
        try:
            p_x = point.x
            p_y = point.y
        except:
            p_x = point[0]
            p_y = point[1]

        try:
            c_x = self.center_point[0]
            c_y = self.center_point[1]
        except:
            c_x = self.center_point.x
            c_y = self.center_point.y

        dis = math.sqrt((c_x - p_x)**2 + (c_y - p_y)**2)

        if dis > self.radius:
            return f"{point}点在圆外"
        elif dis < self.radius:
            return f"{point}点在圆内"
        else:
            return f"{point}点在圆上"

p = Point(9,0)

c1 = Circle((3,4),5)  #直接传元组的圆
c2 = Circle(p,5)      #传Point类的圆
print(c1.perimeter())
print(c1.position_with_point(p))

print(c2.position_with_point(p))