import sys,os
#os.rename("1.1内置模块1.1.py","1.1内置模块sys.py")#修改文件名

print("hello")
print("wo")

print(sys.path) #系统工作路径
sys.stdin  #标准输入,类似于循环输入
sys.stdout #标准输出，指定输出位置，不一定是控制台
sys.stderr #指定输出错误位置，用于保存错误日志
sys.exit(90) #更改退出码,终止程序运行
