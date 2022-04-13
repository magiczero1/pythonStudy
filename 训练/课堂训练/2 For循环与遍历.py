'''for i in range(10):#循环
    print(i)
print("----------")'''
#遍历的第一种写法，直接遍历对象
a = "你好，我是贝尔机器人的拾壹"  #a是一个变量，现在也是一个遍历的对象
b = ["acd","m16","98k",11,16,"好的"]
for i in a:
    print(i)
#遍历的第二种写法，利用索引遍历对象
for i in range(len(a)):
    print(a[i])