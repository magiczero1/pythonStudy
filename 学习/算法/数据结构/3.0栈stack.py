#利用list来实现栈操作。
class Stack:          #创建一个栈类
    def __init__(self):
        self.items =[]            #初始化一个空列表，即实际上栈是一个列表
    def isEmpty(self):
        return self.items == []   #若栈为空，则列表为空
    def push(self,item):
        self.items.append(item)   #定义栈的数据进入方向为从末端进入
    def pop(self):
        return self.items.pop()          #定义栈的数据出去方向为末端出去，默认返回pop()抛出末尾的数据
    def peek(self):
        return self.items[len(self.items)-1] #返回栈的底端值
    def size(self):
        return len(self.items)               #返回栈的长度