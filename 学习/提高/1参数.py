#放在函数名中的叫做形参(仅限于函数体中占位使用，可初始化)

def add(a=10,b=1):      #a,b叫做形参,  赋值操作叫做初始化
    return a+b

print(add())
print("-"*20)
print(add(1,2))    # 1，2叫做实参
