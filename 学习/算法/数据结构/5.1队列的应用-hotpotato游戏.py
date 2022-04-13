# 给定一组数据，前面为人数，逢7就出列
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

def hotPotato(nameList,num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["a","b","C","d","e","f"],7))