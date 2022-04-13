#字典 以键-值对存在的.键不可变，值可变
#a={'a':97}
# key键-值value

#创建字典
'''
a={}#空字典
scores1={'李白':98,'张三':73,'狗儿':15,'刘大鹅':99}  #第一种直接创建
scores2=dict({'李白':98,'张三':73,'狗儿':15,'刘大鹅':99}) #第二种利用函数进行赋值创建,注意（）
print(scores2)
'''
#获取字典中的值[]与.get()
'''
scores1={'李白':98,'张三':73,'狗儿':15,'刘大鹅':99}
print(scores1['李白'])
print(scores1.get('李白'))
#print(scores1['李太白'])#会报错
print(scores1.get('李太白'))#不会报错，直接返回默认值None
print(scores1.get('李太白',100))#不会报错，直接返回默认值100
'''
#字典的增删改
'''
scores1={'李白':98,'张三':73,'狗儿':15,'刘大鹅':99}
scores1['天天']=67 #增
print(scores1)
del scores1['李白']
print(scores1)  #删
scores1['李白']=['李太白']
print(scores1)  #改  注意只能改值
scores1.clear()
print(scores1)  #清空字典
'''
#获取所有的键元素.keys，值元素.values 键-值.items
'''
scores1={'李白':98,'张三':73,'狗儿':15,'刘大鹅':99}
print(scores1.keys())
print(scores1.values())
print(scores1.items())#获取的对象为元组
'''
#字典生成式，利用zip()打包列表内的元素，并生成元组
a=['北京','上海','成都','南京']
b=[10,12,21,'a']#注意不能以0开头，若以0开头则会数据报错
c={a:b for a,b in zip(a,b)}
print(c.get("北京"))