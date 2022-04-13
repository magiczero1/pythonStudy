#中缀A+B     前缀 +AB     后缀AB+
#定义三种运算逻辑
#中  A+B*C+D  →  前 ++A*BCD  → 后((A(BC*)+)D+)    去掉括号就是表达式
#中  (A+B)*(C+D)  →  前*+AB+CD   → AB+CD+*=
#中  A+B+C+D  →  前 +++ABCD  → 后ABCD++

class Stack:          #创建一个栈类
    def __init__(self):
        self.items =[]            #初始化一个空列表，即实际上栈是一个列表
    def isEmpty(self):
        return self.items == []   #若栈为空，则列表为空
    def push(self,item):
        self.items.append(item)   #定义栈的数据进入方向为从末端进入
    def pop(self):
        self.items.pop()          #定义栈的数据出去方向为末端出去，pop()默认抛出末尾的数据
    def peek(self):
        return self.items[len(self.items)-1] #返回栈的底端值
    def size(self):
        return len(self.items)               #返回栈的长度

def infixnToPostfix(abc): #传入参数必须要用空格隔开，否则转化为列表进行分割
    tokenList = abc.split(" ")     #如传入 A*B+C*D   → AB*CD*+      传入的式子为中缀表达式
    #以下定义运算符的优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    #定义运算优先级结束
    opStack = Stack()
    postfixList = []  #初始化后缀表达式
    #以下是判断操作数的代码逻辑
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfixList.append(token)           #将字符放入后缀表达式
        elif token == "(":                      #如果读取到的是"("，就压入栈中
            opStack.push(token)
        elif token == ")":                      #如果读取到的是")"，就抛出栈中的"("进行抵消
            topToken = opStack.pop()
            while topToken != '(':              #重复执行，如果token不是"("，就将token放入postfixList
                postfixList.append(topToken)
                topToken = opStack.pop()
    #判断操作数代码结束
    #以下是判断操作符代码逻辑
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):    #当栈不为空时，判断操作符的优先级
                postfixList.append(opStack.pop())
                opStack.push(token)
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)                 #返回值为空，不明白``````
print(infixnToPostfix(" ( ( A + B ) * ( C + D ) ) "))
