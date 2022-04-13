import random
str = "abcdefghijklmn"
list1 = ['g', 'l', 'h', 'j', 'l', 'g', 'j', 'b', 'l', 'j', 'l', 'f', 'c', 'g', 'l', 'n', 'l', 'h', 'n', 'k']

for i in range(20):
    list1.append(random.choice(str))

dict1 = {}
for i in list1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for k,v in dict1.items():
    if v == max(dict1.values()):
        print("出现次数最多的字母是%s,出现了%d次"%(k,v))