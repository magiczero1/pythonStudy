#单分支
'''
if 2>10:
    print('ok')
print('no')
'''
#双分支
'''
if 5>8:
    print('Ok')  #条件为真时输出Ok
else:
    print('No')  #条件为假时输出No
    
money=1000.0
s=input('请输入取款金额：')
if float(s)>money:
    print('您的余额不足。')
else:
    print('您成功取款%.2f元'%float(s),'余额为%.2f'%(money-float(s)))
'''
#多分支
'''
cat_type='white'
if cat_type=='black':    #注意判断的时候要用==，而不是=
    print('1you are wrong，please try again')
elif cat_type=='blue':
    print('2you are wrong，please try again')
elif cat_type=='orange':
    print('3you are wrong，please try again')
else:
    print("It's a white cat") #单引号一定要放在双引号内
'''
#嵌套if
'''
price=float(input('请输入购物金额：'))
member=input('您是会员吗？y/n：')
if member=='y':
    if price>=200:
        print('您应该支付的金额为%.2f*0.8=%.2f'%(price,price*0.8))
    elif price<200 and price>=100:
        print('您应该支付的金额为%.2f*0.9=%.2f'%(price,price*0.9))
    else:
        print('您应该支付的金额为%.2f'%price)
else:
    print('您应该支付的金额为%.2f'%price)
'''
#等价写法
#第一种写法
a=input('输入第一个数：')
b=input('输入第二个数：')
if int(a)>int(b):
    print(a+'大于等于'+b)
else:
    print(a+'小于'+b)
#第二种写法
a=input('输入第一个数：')
b=input('输入第二个数：')
print(a+'大于等于'+b  if int(a)>int(b) else a+'小于'+b)