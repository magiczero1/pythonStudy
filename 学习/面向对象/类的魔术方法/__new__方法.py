#__new__构造方法（默认从object继承）
#触发时间：实例化对象同时触发
#作用：管理控制对象控制过程
#参数：一个cls接收当前的类，其他参数根据实例化对象决定
#返回值：可有可无，没有实例化对象返回NONE
#注意事项：
class Human():
    def __new__(cls,sex,*args, **kwargs):#
        #自己控制对象的生成过程
        if sex =="女":
            object.__new__(cls)#python中的上帝之手，cls是class简写
            print("是一个女儿")
    def eat(self):
        print("吃饭方法")
    def sleep(self):
        print("睡觉方法")
    def sport(self):
        print("运动方法")
two=Human("男")#实例化对象 【a】制作一个对象【2】初始化实例对象