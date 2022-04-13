import json
#evel

a = "1+1"
print(eval(a))

#json  轻量级数据交换
'''转换规则'''
#Python    →        json
#字符串              字符串
#字典                对象
#列表、元组、集合      数组

list = [1,2,3,4,5]
dict = {"name":"zhangsan","age":18,"gender":"female"}

#dums转字符串
y = json.dumps(dict)
x = json.dumps(list)
print(type(x))
print(type(y))

#loads 还原部分数据的源数据格式，如str、list、dict等
JSON = '[1,2,3,4]'
z = json.loads(JSON)
print(type(z))

