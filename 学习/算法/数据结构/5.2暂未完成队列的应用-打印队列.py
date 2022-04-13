class Queue:     #以左端为首，右端为尾
    def __init__(self):
        self.items = []        #初始化不需要返回值
    def enqueue(self,item):    #进队列
        self.items.append(item)
    def dequeue(self):         #出队列
        return self.items.pop(0)
    def isEmpty(self):
        return bool(self.items == [])
    def size(self):
        return len(self.items)
    def clear(self):
        return self.items.clear()
import random
#场景假设：每小时有10个学生，每个学生提交10~20页的打印需求
#以下为仿真任务的逻辑流程
#明确任务对象： ①打印任务的属性：提交时间、页数  ②打印队列的属性：具有FIFO性质的打印任务队列   ③打印机的属性：是否在忙，打印速度
#明确打印作业的生成概率：（以最大任务需求为模拟）则1个task/20p 的概率为 20p/1h  = 1p/180s   如打印10页，需要1/18s
'''
以下为任务实现流程
*创建打印队列对象
*时间按照一个单位（1s）的单位流逝
*时间用尽，开始统计平均等待时间
'''
class Printer():
    def printTask(self,nums):        #①打印任务的属性：提交时间、页数
        uploadTime = self
        uploadPaernums = nums

    def printQueue(self):           #②打印队列的属性：具有FIFO性质的打印任务队列
        a = Queue()

    def printerState(self):         #③打印机的属性：是否在忙，打印速度
        isBusy = False
        speed1 = 5
        spped2 = 10