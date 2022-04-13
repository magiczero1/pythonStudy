from io import StringIO
from io import BytesIO   #二进制读写，用法类似于StringIO

#StringIO 写入内存
s_io = StringIO() #实例化一个对象
s_io.write("你好")
s_io.write("Python")

x = s_io.read()  #此时在内存中，无法直接读取,返回空值
print(x)

cont = s_io.getvalue() #一次性取出所有值
print(cont)


#print 进阶用法
#print(值,file = s_io)  暂时打印到缓存中
print("嘿嘿嘿",file=s_io)
print("嘻嘻嘻",file=s_io)
print("hahah",file=s_io)

print(s_io.getvalue())

#print(值，file = open(path,"w"))
print("print的进阶用法",file=open("读写测试.txt","a"))

s_io.close()#读写完之后，还是需要关闭