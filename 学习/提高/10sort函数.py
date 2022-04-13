#sort()不生成新空间，原有基础上排序
list1 = [1,4,5,51,31,13,2]
print("原来的地址0x%X"%id(list1))
list1.sort()
print("排序后的地址0x%X"%id(list1))
print(list1)


dict1 = [
    {"name":"zhangsan","age":18,"gender":"male"},
    {"name": "lisi", "age": 22, "gender": "female"},
    {"name": "Rick", "age": 27, "gender": "male"},
    {"name": "Shooby", "age": 6, "gender": "female"}

]

def foo(arg):
    return arg["age"]

dict1.sort(key=foo)   #可通过对某个数据进行遍历取值，然后排序
print("按年龄排序后的数据：",dict1)

dict1.sort(key = lambda arg:arg["gender"])   #可使用匿名函数指定排序的数据项
print(dict1)

#sorted()生成新空间
list2 = [1,4,5,51,31,13,2]
sorted(list2)
print(list2)      #直接打印没有变化
new_list = sorted(list2)
print(new_list)   #必须通过赋值操作进行输出