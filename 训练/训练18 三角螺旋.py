import turtle
t = turtle

'''
def triangleSpiral(size):
    if size > 0:
        t.forward(size)
        t.right(120)
        triangleSpiral(size-5)

triangleSpiral(100)
t.done()'''

def triangleSpiral2(size):
    if size < 100:
        t.forward(size)
        t.right(120)
        triangleSpiral2(size+5)

triangleSpiral2(0)
t.done()