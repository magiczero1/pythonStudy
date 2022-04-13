#先进先出    常见应用：进程调度、键盘输入、缓存
class Queue:
    def __init__(self):
        self.items = []        #初始化不需要返回值
    def enqueue(self,item):    #进队列
        self.items.append(item)
    def dequeue(self):         #出队列
        self.items.pop(0)
    def isEmpty(self):
        return bool(self.items == [])
    def size(self):
        return len(self.items)
