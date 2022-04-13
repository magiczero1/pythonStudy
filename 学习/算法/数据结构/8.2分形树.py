#分形Fractal
import turtle as T
def fractalTree(branch_len):
    if branch_len > 5:
        T.forward(branch_len)   #画主干
        T.right(20)
        fractalTree(branch_len-15)  #画右分支
        T.left(40)
        fractalTree(branch_len-15) #画左分支
        T.right(20)
        T.backward(branch_len)     #回到原位置

T.setheading(90)
fractalTree(100)
T.done()