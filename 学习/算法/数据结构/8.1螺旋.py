import turtle as T
def drawSpiral(lineLen):
    if lineLen > 0:
        T.forward(lineLen)
        T.right(90)
        drawSpiral(lineLen-1)

def drawSpiral2(lineLen):
    if lineLen < 200:
        T.forward(lineLen)
        T.left(90)
        drawSpiral(lineLen+10)

T.speed(10)
drawSpiral(100)
T.hideturtle()
T.done()