import sys

#sys.stdin  标准输入类，可以被读取
s_in = sys.stdin  #读取键盘输入的内容
'''while True:
    cont = s_in.readline()  #读取标准输入位置的一行数据
    if cont == "\n":
        break
    print(cont)
'''

#sys.stdout 标准输出类，可以选择输出的位置：控制台、文件、服务器等等
#写完该语句后的后续所有输出将输出到指定位置
sys.stdout = open("指定输出台.txt","a",encoding="utf-8")
print("你好")
print("哈哈哈哈")
#print(a)  #此时的错误还是输出在控制台

#sys.stderr
sys.stderr = open('错误日志.txt',"a",encoding="utf-8")
#print(a) #已经将错误写入到错误日志中
print(1/0)