#注意字符串、元组一旦修改，对应的id也会改变，而列表、集合、字典不会
s="hello,python"
print(s[:5])
print(s[6:])
print(s[:5]+s[6:])
print(s[::-1])

name1=["张三","李白","韩信","廉颇"]
name2=["李白","韩信","廉颇"]
for i in range(3):
    if name2[i] in name1:
        print(f'{name2[i]}是王者荣耀中的英雄')