#r 只读
#w 只写
#a 追加
#rb/wb  只读只写二进制文件，如doc、png、jpg等
#*+ 读写模式  必须和上面的之前的连用

b=open(r"/读写文件/冰墩墩代码.txt", "a+")
b.write("哈哈哈哈")
b.close()
print(b)

with open(r"/读写文件/c.txt", "r+") as file1:
    #file1.write("用程序做软件")
    print(file1.read(3))#read中控制输出字符数