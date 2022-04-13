import turtle as T
T.screensize(1440,800,"blue")#设置绘图区大小，默认400*300
T.speed(300)#设置绘图速度，a-10之间

'''
T.circle(105)#向右画半径为105的圆
T.circle(-105)#向左画半径为105的圆
T.forward(100)#画长度为100的直线，默认向前
T.backward(100)#画长度为100的直线，默认向后
T.left(90)#左转90°
T.right(90)#右转90°
T.setx(0)#设置当前坐标为x轴
T.sety(0)#设置当前坐标为y轴
T.setheading(90)#设置朝向为90°方向
T.home()#回到原点
T.dot(600,"red")
'''#绘图指令
'''
T.pen("pencil")
T.pendown()#默认落笔
T.penup()#默认落笔
T.pensize(10)#设置笔的大小
T.pencolor("red")#设置颜色lor(colorstring)#绘制图形的填充颜色
T.color(color1, color2)#同时设置pencolor=color1, fillcolor=color2
T.filling()#返回当前是否在填充状态
T.begin_fill()#准备开始填充图形
T.end_fill()#填充完成
T.hideturtle()#隐藏画笔的turtle形状
T.showturtle()#显示画笔的turtle形状
'''#画笔指令
# coding=utf-8
import turtle
import time

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("中国", font=('Arial', 40, 'normal'))
turtle.goto(-120, -120)

turtle.mainloop()