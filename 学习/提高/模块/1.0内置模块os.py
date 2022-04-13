#os 用来调用系统的模块
import os

print(os.name)  #获取操作系统的名称    windows→nt    mac→posix
print(os.sep)   #获取路径分隔符
#os.getcwd() 获取当前工作路径
#os.chdir()  切换路径
#os.mkdir()  在当前路径下生成文件夹
#os.mkdir("你好") #创建 你好 文件夹
#os.rename("循环模块.py","09循环模块.py")
print(os.listdir())#列出当前文件夹的所有目录及文件
print(os.listdir("/Users/mac/PycharmProjects/pythonProject1/学习/提高"))#列出当前文件夹内所有的文件




#常用的os.path
print(os.path.abspath("0模块基础.py"))  #获取文件的绝对路径
print(os.path.isdir("0模块基础.py")) #判断是否是文件夹
print(os.path.isfile("0模块基础.py")) #判断是否是文件