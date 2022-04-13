#一个进程包含1个或多个线程
#进程是资源单位
#线程是执行单位
from threading import Thread    #导入线程类
'''第一种写法，使用Thread模块+函数进行多线程创建'''
'''
def fun():
    for i in range(100):
        print("fun",i)
def fun2():
    for i in range(100,200):
        print("fun2",i)

t = Thread(target=fun)
t2 = Thread(target=fun2)
t.start()
t2.start()
for i in range(101):
    print("main",i)
'''
'''第二种写法，继承Thread类，再进行多线程.具体的执行顺序由CPU决定，跟CPU线程数有关'''
'''class mythread(Thread):
    def run(name):#固定写法
        for i in range(1000):
            print(i,name)'''

def func(name):
    print(name)

if __name__ == '__main__':
    t1 = Thread(target=func,args=("周杰伦",))#利用args传参，参数属性必须是tuple
    t1.start()

    t2 = Thread(target=func("李天宇"))#直接传参就无所谓
    t2.start()