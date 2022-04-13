import copy
x = ["hello","hi",[1,3,5],"ok","good"]
#赋值操作
y = x
print(id(x),id(y))
x[1] = 99
print(y[1])

#浅拷贝
z = x.copy()   #浅拷贝，会生成新的地址
x[1] = 100     #拷贝后更改源列表的数据，数据产生变化
print(z,id(x),id(z))#输出新数据

#深拷贝,
a = copy.deepcopy(x)  #深拷贝，会生成新的地址
x[1]=100       #拷贝后更改源列表的数据，数据！不！产生变化
print(a,id(a),id(x))

