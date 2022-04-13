import os #导入os模块
file_name = input("请输入文件路径")
if os.path.isfile(file_name):   #判断文件是否存在
    old_file = open(file_name,"r")
    content = old_file.read()
    old_file.close()

    new_file = open(file_name.replace(".",".bak."),"w",encoding="utf-8")
    new_file.write(content)
    new_file.close()
    print("ok")

else:
    print("小giegie，文件读取出错咯")