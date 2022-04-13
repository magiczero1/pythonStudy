#try except except``````用来定位可能出现的已知类型错误
def fun1(*args):
    try:
        a=int(input('被除数'))
        b=int(input("除数"))
        c=a/b
        print('商',c)
    except ZeroDivisionError:
        print("0不准做除数")
        fun1()
    except ValueError:
        print("不准输入字母")
        fun1()  #
fun1(999999,999)

#try except B  as e    else     finally用来定位未知的错误，并最终执行既定代码
def fun2(*args):
    try:
        x=int(input("加数1"))
        y=int(input("加数1"))
        z=x+y
    except BaseException as e:
        print("错误是",e)
    else:
        print('和是',z)
    finally:
        fun2()