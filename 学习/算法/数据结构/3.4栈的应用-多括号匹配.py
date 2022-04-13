#多括号匹配的天才构思来自于 双栈的实现，即成对出现的括号，在不同的栈中，都会按照一定的顺序进行匹配。
class Stack:          #创建一个栈类
    def __init__(self):
        self.items =[]            #初始化一个空列表，即实际上栈是一个列表
    def isEmpty(self):
        return self.items == []   #若栈为空，则列表为空
    def push(self,item):
        self.items.append(item)   #定义栈的数据进入方向为从末端进入
    def pop(self):
        return self.items.pop()          #定义栈的数据出去方向为末端出去，pop()默认抛出末尾的数据
    def peek(self):
        return self.items[len(self.items)-1] #返回栈的底端值
    def size(self):
        return len(self.items)               #返回栈的长度
#以下判断()是否成对的前提条件是所有元素为'('，')'二者之一
def parChecker(symbolString):
    s = Stack()        #创建一个空栈s
    balanced = True    #初始化平衡制为1,约束条件
    index = 0          #初始化索引值
    while index <len(symbolString) and balanced:
        symbol = symbolString[index]     # 对象遍历、写入变量symbol
        if symbol in "([{":              #'''更新对象，并将判断条件更改为in'''
            s.push(symbol)               # 则加入栈s
        else:
            if s.isEmpty():              #判断栈对象元素为空
                balanced = False         #更新balanced
            else:
                top  = s.pop()                  #抛出栈顶元素，并存入top中
                if  not matches(top,symbol):     #引入新函数matches，对抛出元素与右侧括号进行匹配
                    balanced = False
        index += 1
    #以下进行最终判断
    if s.isEmpty() and balanced:
        return True
    else:
        return False

def matches(left,right):
    lefts = "([{"
    rights = ")]}"       #注意匹配顺序
    return lefts.index(left) == rights.index(right)


print(parChecker('[{((()))}]'))  #返回 [空] 类型是因为类中没有return pop值
