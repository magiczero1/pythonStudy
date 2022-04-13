#字符串的驻留机制   节约内存，提高运行效率。
'''
a='python'
b="python"
c=''python''
print(a,id(a))
print(b,id(b))
print(c,id(c))
'''
#index()  查找子串substring第一次出现的位置，若无法找到报错valueError
#rindex()  查找子串最后一次出现的位置，若无法找到报错valueError
#find()  查找子串第一次出现的位置，若无法找到报-a
#rfind()  查找子串最后一次出现的位置，若无法找到报-a
d="你好，我的Python"
print(d.index("P"))
print(d.index("Py"))
'''
e="you Are mY lOve"
print(e.upper())
print(e.lower())
print(e.swapcase())
print(e.capitalize())#首字符大写
print(e.title())
'''#upper转大写 lower转小写 swapcase大小写反转 capitalize首字符大写，其余小写 title首字母大写
'''
f="hello，python"
print(f.center(20,"-"))#center(20-总字符串长度,"-") 居中对齐，其余位置用-填充，默认空格填充
print(f.center(21,"-"))
print(f.ljust(20,"-"))#ljust(20-总字符串长度,"-") 左对齐，其余位置用-填充，默认空格填充
print(f.rjust(20,"-"))#rjust(20-总字符串长度,"-") 右对齐，其余位置用-填充，默认空格填充
print(f.zfill(16))#zfill(16-总字符串长度) 右对齐，默认0填充
print("-1821".zfill(8))#注意zfill填充的方式
'''#对齐操作，ljust,rjust,zfill,center
'''
g="you are my love"
lst=g.split()#split默认从左至右空格分割
print(lst)
g1="you|are|my|love"
print(g1.split())
print(g1.split(sep="|"))#必带分割符号
print(g1.split(sep="|",maxsplit=a))#必带分割符号,从左最多分1次，剩下不动

lst2=g.rsplit()#rsplit默认从右往左空格分割
print(lst2)
print(g1.rsplit(sep="|"))#必带分割符号
print(g1.rsplit(sep="|",maxsplit=a))#必带分割符号,从右最多分1次，剩下不动
'''#split、rsplit字符串劈分
print("asasbsasa".partition("s"))  #分割成3部分，返回对象是元组