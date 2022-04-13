import pickle
#pickle可以存储所有拿到的数据，但是只支持python解释器的解码。

#序列化：dumps   dump
#反序列化：load loads

names = ["张三","李四","二麻子","Rosie"]

#dumps  返回二进制数据
x = pickle.dumps(names)
print(x)

#loads  解码二进制数据
print(pickle.loads(x))

#dump   将二进制数据储存到指定文件里
file = open("二进制读写.txt","wb")
y = pickle.dump(names,file)
file.close()

#load 从文件中读取二进制数据
file = open("二进制读写.txt","rb")
print(pickle.load(file))
file.close()