#__call__集合调用
#触发时间：将对象当做函数调用时自动触发one（）
#作用：常用于调用一系列的方法
#参数：self接收当前对象，其他参数接收附加对象。
#返回值：return 可有可无
#注意事项：
class Oneday():
    name = "张三"
    age  = 18
    def openeye(self):
        print("睁眼")
    def getup(self):
        print("起床")
    def wash(self):
        print("洗漱")
    def gotoschool(self):
        print("上学")
    def clothclean(self):
        print("洗衣服")
    def __call__(self,name):
        self.openeye()
        self.getup()
        self.wash()
        self.gotoschool()
        self.name=name
        print("{}开始了新的一天".format(name))
one = Oneday()
print(one)
one('张三')#将张三传入__call__的参数中