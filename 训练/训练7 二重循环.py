#break  跳出内层循环
#continue 继续内层循环
#注意二者区别，一般循环嵌套为3层。
for i in range(5):
    for j in range(1,10):
        if  j%2==0:
            print(j,'是偶数',end="\t")
            #break#跳出当前循环体
            continue
    print( )