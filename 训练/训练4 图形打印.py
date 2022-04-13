#打印三角形（注意联系九九乘法表）
for a in range(1,10):
    print("*"*a,end='\n')
print( )

#打印矩形
c=int(input('请输入矩形的宽：'))
a=0
b=int(input('请输入矩形的长：'))
if b>=c:
    while a<c:
        print(" * "*b,end='\n')
        a+=1
else:
    print("输入错误，请保证长度大于等于宽度哦")
