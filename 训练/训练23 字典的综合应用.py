persons = [
    {"name":"zhangsan","age":18},
    {"name":"lisi","age":22},
    {"name":"Jerry","age":12},
    {"name":"Tomas","age":31}
]
name = input("请输入姓名")

def add(name,age):
    values = {"name":name,"age":age}
    return values

for i in range(len(persons)):
    if name == persons[i]["name"]:
        print("已存在相同名字")
        break
else:       #注意外层循环
    age = int(input("请输入用户年龄"))
    persons.append(add(name,age))

print(persons)

