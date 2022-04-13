#无序表中需要初始化一个头节点
class Node:         #声明一个Node类
    def __init__(self,initdata):
        self.data = initdata       #数据域
        self.next = None            #将下一项设为空
    def getData(self):
        return self.data            #获取数据
    def getNext(self):
        return self.next            #指向下一组数据
    def setData(self,newdata):
        self.data = newdata         #修改数据
    def setNext(self,newnext):
        self.next = newnext         #修改指针

class UnorderedList:
    def __init__(self):
        self.head = None

class MyList(Node,UnorderedList):

    def add(self,item):
        temp = Node(item)         #生成一个临时节点
        temp.setNext(self.head)   #将链接指向新head
        self.head = temp          #重写入数据

    def size(self):               #用循环得到size
        current = self.head
        count = 0
        while current != None:
            count += 1
        return count

    def search(self,item):       #寻找的时候也必须从头开始寻找
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):   #要先将前(previous)一个节点指向后一个节点，然后再释放当前节点(current)。否则数据会丢失
        current  = self.head
        previous  = None
        found = False
        while not found:
            if current.getData() == item:
                found  = True
            else:
                previous = current          #利用双指针一前一后进行操作
                current = current.getNext()
        if previous == None:
            self.head  = current.getNext()
        else:
            previous.setNext(current.getNext())#前节点指向后节点


MyList(93)
MyList(33)

print(MyList.getData(33))