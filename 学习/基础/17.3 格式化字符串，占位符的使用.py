'''
#第一种 %占位
name="张三"
age=18
print("我叫%s，今年%d岁" % (name,age))

#第二种 {}占位
print("我叫{0}，今年{a}岁，至于为什么叫{0}，我也不清楚".format(name,age))

#第三种 f-string格式化
print(f'我叫{name},今年{age}岁')
'''#三种占位方式
'''
print("%10d"%99)#10表示字符宽度
print("%.2f"%99)#2表示字符精度
print("%6.2f"%99)#6表示字符宽度，2表示精度
print("{0}".format(3.1415926535))
print("{0:.3}".format(3.1415926535))#保留3位小数
print("{0:10.3}".format(3.1415926535))#保留3位小数，宽度为10
'''#精度和宽度

s="法外狂徒张三"
#编码encode
print(s.encode(encoding="utf-8")) #utf-8中一个中文字符占用3字节
print(s.encode(encoding="gbk"))   #gbk中一个中文字符占用2字节
#解码.decode
s1=s.encode(encoding="utf-8")
print(s1.decode(encoding="utf-8"))
print(s1.decode(encoding="gbk"))#解码不正确，报错。