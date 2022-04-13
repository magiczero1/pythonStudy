#链表中的内容是无序的

#链表中的基本结构——节点Node
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

temp = Node(93)
temp.getData()