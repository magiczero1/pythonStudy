#完美散列方法3：转换累加法

#如对cat散列,首先对字符进行ASCII反转编码,槽数tablesize
#-----基础版，直接累加-------
def strHash(str,tablesize):
    sum = 0
    for i in str:
        sum += ord(i)
    return sum%tablesize

#针对变位词
#-----进阶版，权重累加-------
def strHash2(str,tablesize):
    sum = 0
    for i in range(len(str)):
        sum += ord(str[i])*(i+1)
    return sum%tablesize

print(strHash2("cat",11))