'''
a=int(input('请输入想转化的数字'))
print(bin(a))
print(oct(a))
print(hex(a))

print(chr(97))#输出ASC2码对应的字符
print(ord('a'))
'''
a=chr(97)
print(ord(a))
print('a的二进制是'+bin(ord(a)))#将a的asc2进行二进制转化
print('a的八进制是'+oct(ord(a)))
print('a的十六进制是'+hex(ord(a)))
print(ord(a)/3)   #除法
c=ord(a)/3
print("%.2f"%c)   #求模（余数）

print(ord(a)//3)  #整除
print(len(a))

b=ord(a)>>2
print(b)#将a的asc2进行左移运算
print(oct(b))
print(hex(b))
