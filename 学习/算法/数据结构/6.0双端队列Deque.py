#双端队列具有栈和队列的集成特性，但须有使用者自行维护。
#前端操作：复杂度O(1)      尾端操作：复杂度O(n)
class Deque:
    def __init__(self):
        self.items= []
    def isEmpty(self):
        return bool(self.items)
    def addFront(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        self.items.pop(0)
    def addRear(self,item):
        self.items.append(item)
    def removeRear(self):
        self.items.pop()
    def size(self):
        return len(self.items)