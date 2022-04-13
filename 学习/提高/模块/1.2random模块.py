import random

print(random.random()) #生成[0，1)的随机小数
print(random.randint(1, 100)) #生成[1，100]的随机整数
print(random.randrange(2, 9)) #生成[2，9)的随机整数

list1 = ["张三","李四","Jerry","Kel","Didi"]
print(random.choice(list1)) #针对可迭代对象随机抽取一个
print(random.choices(list1,k=100)) #针对可迭代对象随机抽取k个，可重复抽取
print(random.sample(list1,2)) #针对可迭代对象随机抽取n个，不可重复抽取，返回列表