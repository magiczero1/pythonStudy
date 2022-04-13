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

class OrderedList:
    def __init__(self):
        self.head = None

class MyList2(Node,OrderedList):
   #与无序表最大的区别在于add，要保证前后的有序性
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        #不断更新当前节点以及前节点，发现插入位置
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)         #生成一个临时节点

        if previous == None:        #数据插在表头
            temp.setNext(self.head)   #将链接指向新head
            self.head = temp          #重写入数据
        else:                       #数据插在表中
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):               #用循环得到size
        current = self.head
        count = 0
        while current != None:
            count += 1
        return count

    def search(self,item):       #寻找的时候也必须从头开始寻找
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:  #与无序表相比，有序表可以多一个判断用于节约时间
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:   #用于判断是否停止
                    stop = True
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


MyList2(93)
MyList2(33)

print(MyList2.getData(33))