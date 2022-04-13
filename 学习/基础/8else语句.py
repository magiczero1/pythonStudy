#else可与while、if、for联合使用
'''
for a in range(3):
    pwd=input("请输入密码")
    if pwd=='8888':
        print('密码正确')
    else:
        print('密码不正确')
else:
    print('连续输错3次密码，您的账号已锁定。')
'''#第一种写法，for else，注意for已经对a进行了赋值，所以不用初始化a
'''
a=0
while a <3:
    pwd = input("请输入密码")
    if pwd == '8888':
        print('密码正确')
    else:
        print('密码不正确')
    a+=a
else:
    print('连续输错3次密码，您的账号已锁定。')
'''#第二种写法，while else 注意while一定要对a进行赋值，所以一定要指定范围，并且对a进行变量自增处理