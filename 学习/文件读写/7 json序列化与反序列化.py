#序列化：让数据按照一定方式写入某种存储工具中
#反序列化：从存储工具中读取数据
import json
#json保存的信息具有局限性

#使用json将数据转化成 特殊的字符串  ' "","","" '
names = ['zhangsan',"lisi","JAck","rose"]
spend = {"吃饭":90,"洗脚":666}

#json.dumps  ：只是将数据转化成json字符串，可以传参，但无法直接指定写入位置
x = json.dumps(names)
y = json.dumps(spend)

file = open("json数据读写测试.txt","a",encoding="utf8")
#file.write(x)
#file.write(y)


#json.dump :将数据转化成json字符串，并写入指定位置
#json.dump(names,file)
file.close()

#反序列化
#json.loads 将json字符串加载成为python里的数据
#json.load 将文件中的json字符串加载成为python里的数据
print(json.loads(y)) #注意此时只有值

file1 = open("json数据读写测试.txt","r",encoding="utf-8")
print(json.load(file1)) #此时是从文件中读取json字符串
file1.close()
