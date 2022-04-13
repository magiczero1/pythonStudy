#形如def  add()   这样的就叫做函数，可用pass占位
#函数三要数：函数名、参数、返回值
def add1():   #定义函数名
    pass     #函数体

def add2():   #无参数函数
    a = 1       #局部变量
    b = 2
    return a+b  #返回值(必须单独由print打印出来)

print(add2())

#global全局变量
word = "ok"

def output():
    a = 100
    global word
    word = "你好"

def output2():
    global word
    word = "我不好"

output()    #实例化之后，全局变量才会生效
print("变量word的值是{}".format(word))

'''查看局部变量和全局变量'''
print("output函数中局部变量是{0},全局变量是{1}".format(locals(),globals()))