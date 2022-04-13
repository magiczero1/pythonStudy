#__str__
#触发时间：【a】使用print打印对象时自动触发【2】使用str（）转换数据类型时
#作用：自定义打印对象显示的信息
#参数：一个self接收当前对象
#返回值：必须是字符串类型
#注意事项：无

class Poem:
    country=["中","希腊","美","德"]
    def __str__(self):
        return self.country[0]
    def poet(self):
        print("维多利亚、砸瓦鲁多、李白白")
    def liupai(self):
        print("自由诗、浪漫诗、古体诗")
sr=Poem()
print(sr.poet())