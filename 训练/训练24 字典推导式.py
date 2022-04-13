dict1 = {"a":100,"b":200,"c":300}
dict2 = {x:y for y,x in dict1.items() }
print(dict2)