file = open("二进制读写.txt","rt")
x = file.read(3)  #读取n个字符，优化读取速度（可循环读取）
file.close()

print(x)