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

def palChecker(aString):
    deque  = Deque()
    for i in aString:
        deque.addFront(i)

    stillEqual = True
    while deque.size() > 1 and stillEqual:
            front = deque.removeFront()
            tail = deque.removeRear()
            if front != tail :
                stillEqual = False

    return stillEqual

print(palChecker("asasall"))