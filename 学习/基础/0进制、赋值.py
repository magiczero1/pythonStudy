print(0b11110)#0b   0B  二进制
print(bin(14))#将14转化为2进制

print(0o11110)#0o  0O 八进制
print(oct(4680))

print(0x11110)#0x  0X  十六进制
print(hex(69904))

#链式赋值，赋值一致
a=b=c=1
print(a)
print(b)
print(c)

#多重赋值，同时为多个变量赋值，赋值可不一致
x,y=1,2
x,y=y,x#变量交换，超牛的功能
print(x)
print(y)

#增量赋值
s=115
s%=5
print(s)

#利用eval()进行特殊赋值
m="10,20,30"
u,v,z=eval(m)
print(type(u))
print(v)
print(z)


print(int("17",8))#将八进制数17以10进制输出