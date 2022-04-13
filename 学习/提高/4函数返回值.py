def math(num1,num2):
    x = num1 * num2
    y = num1 % num2
    z = num1 // num2
    return {"积":x,"商":z,"余":y}   #可以返回字典

def test(a,b):
    return a//b,a*b    #默认返回元组

print(type(test(3,5)))

print(math(10,6))
