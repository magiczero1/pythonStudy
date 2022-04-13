#os.sep 查看系统的分隔符   Windows一般"\"  其他的"/"

#路径：
#绝对路径（可能不适用于其他电脑，因此个人开发时可以选择使用）：/Users/mac/PycharmProjects/pythonProject1/学习/文件读写/1 文件操作.py
#相对路径（用处广泛一些）：1 文件操作.py          ①默认从当前文件夹开始，可写"./"，或者不写   ②../ 返回上一级文件夹

'''读写的两种方式'''

#第一种，流程式读写：开-读/写-关
file = open("读写测试.txt",mode="w",encoding="utf-8")
file.write("这是一个测试")
file.close()

#第二种，自闭合读写
with open("读写测试2.txt",mode="w",encoding="utf-8") as file1:
    file1.write("这是第二个测试")

#二进制写入
file2 = open("二进制读写.txt","wb")
file2.write("二进制读写必须要转码".encode("utf-8"))
file2.close()

with open("二进制读写.txt","rb") as file2:
    print("不解码：",file2.read())

with open("二进制读写.txt", "rb") as file2:
    print("解码后：",file2.read().decode("utf-8"))

