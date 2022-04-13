#平面称为 谢尔宾斯基三角形，立体则称为 谢尔宾斯基金字塔
import turtle as T


def drawTriangle(points,color):  #绘制三角形
        T.fillcolor(color)
        T.penup()
        T.goto(points['top'])
        T.pendown()
        T.begin_fill()
        T.goto(points['left'])
        T.goto(points['right'])
        T.goto(points['top'])
        T.end_fill()

def getMid(p1,p2):     #取中点
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(degree,points):
    colormap = ["lightcyan","salmon","silver","white","cornsilk","royalblue"]
    drawTriangle(points,colormap[degree])
    if degree > 0 :
        #画左边
        sierpinski(degree-1,
                   {
                       "left":points['left'], #　左端点不变
                       "top":getMid(points['left'],points['top']),#　上端点 = (左+上)/2
                       "right":getMid(points['left'],points['right']) #　右端点 = (左+右)/2
                   })
        # 画上边
        sierpinski(degree - 1,
                   {
                       "left":getMid(points['left'], points['top']) ,
                       "top": points['top'],
                       "right":getMid(points['top'], points['right'])
                   })
        # 画右边
        sierpinski(degree - 1,
                   {
                       "left":getMid(points['left'], points['right']),
                       "top": getMid(points['top'], points['right']),
                       "right":points['right']
                   })

points = {
    "left":(-200,-100),
    "top":(0,200),
    "right":(200,-100)
        }
T.speed(10)
sierpinski(4,points)

T.done()