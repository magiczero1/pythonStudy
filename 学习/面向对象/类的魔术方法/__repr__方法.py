#__repr__ 与__str__方法一模一样
#触发时间：在使用repr()时触发
#作用：可以使用repr()返回的操作结果
#参数：一个self接收对象
#返回值：有，且必须是字符串
#注意事项：repr()针对字符串具有还原转义功能，其他如列表对象，与str()功能一致
class Human():
    eyes=2
    name="菊花"
    def eat(self):
        pass
    def sleep(self):
        pass
    def __repr__(self):
        print("repr被触发")
        return "一般情况下repr与str方法一模一样"
one = Human()
print(one)

liric="你存在我深深的\n脑海里"
print("str调用结果是：",str(liric))
print("repr调用结果是：",repr(liric))