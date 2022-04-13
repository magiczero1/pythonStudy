#__len__
#触发时间：使用len()检测对象时自动触发
#作用：
#参数：
#返回值：
#注意事项：
class Car():
    wheels="4"
    def __len__(self):
        num=len(self.wheels)
        return num
    def grand(self):
        print("Benz、BMW、Audi``````")
    def color(self):
        print("blue、yellow")
    def music(  self):
        print("music is coming")
z4=Car()
print(len(z4))#此时检测的是wheels的字符个数，注意数值类型不行