import stack
def postfixEval(postfixExpr):
    operandStack = stack.Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
        else:
            operand2 = int(operandStack.pop())   #注意此时抛出的是peek的值
            operand1 = int(operandStack.pop())  #注意此时是第二次抛出的值
            result = doMath(token,operand1,operand2)
            operandStack.push(result)       #此时要把结果再次存入栈，以防数据遗漏
    return operandStack.pop()

def doMath(op,op1,op2):
    if op =="*":
        return op1 * op2
    elif op =="/":
        return op1 / op2
    if op =="+":
        return op1 + op2
    if op =="-":
        return op1 - op2

print(postfixEval(" 8 8 8 8 + * /"))