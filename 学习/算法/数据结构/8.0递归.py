import sys
#递归：将问题分解为基础元   ①调用自身 ②有停止条件   ！！要防止栈溢出
'''
递归三定律：
1.必须有基本的结束条件，即基础元
2.必须能改变状态，向基本结束条件靠近的调用
3.必须调用自身
'''
#【不用循环进行数列求和】
list = [1,3,5,7,9,11]
def listSum(numlist):
    if len(numlist) == 1:       #最小规模
        return numlist[0]
    else:                       #减小规模
        return numlist[0]+listSum(numlist[1:])

#【任意进制转换】
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]

print(toStr(1020,16))


print(sys.getrecursionlimit())    #查看系统最大栈帧数,可在括号内自行修改。