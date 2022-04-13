import csv

'''读取'''
#open读取
file = open("csv测试文件.csv","r")
x = file.read(15)  #此时会依然会按照字符数多行进行读取
row = file.readline() #读本行的剩下数据
file.close()

print(x)
print(row)

#csv读取
file = open("csv测试写入数据.csv","r")
content = csv.reader(file) #返回一个可迭代对象
for i in content:
    print(i)
file.close()



#open写入(不推荐使用)
file = open("csv测试写入数据.csv","w",encoding="utf-8",newline="\n")  #newline是换行标识,支持转义字符
file.write("张三，")                    #write写入格式，必须是字符串。
file.writelines(("zhangsan","lisi")) #writelines会把可迭代对象全部写入，并且不分割
file.close()

#csv 模块写入
file = open("csv测试写入数据.csv","a",encoding="utf-8")
w = csv.writer(file)  #实例化file对象
w.writerow(["张三","李四"])  #writerow写入数据，将可迭代对象分开写入
w.writerows(["黑，白灰","红黄"])#把可迭代对象中每一个元素以","隔开分开写入；并以","作为换行分隔符。
w.writerows([[1,2,3],[4,5,6],[7,8,9]])
file.close()