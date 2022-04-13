#__del__析构方法（瓦解对象）
#触发时间：【a】主动del对象时触发【2】对象被系统回收的时候自动触发
#作用：回收程序使用过程中的信息和变量等
#参数：self接收当前对象，
#返回值：无
#注意事项：注意触发时机
class Human:

    def run(self):
        pass
    def sleep(self):
        pass
    def __del__(self):
        pass
one=Human()#实例化一个对象
print(one)
