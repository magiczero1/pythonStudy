dict1 = {"name":"zhangsan","age":18,"height":"15cm"}

dict2 = {x:y for x,y in zip(dict1.values(),dict1.keys())}
print(dict2)