#列表生成式
A=[i*i for i in range(1,10)]
print(A)
#集合生成式 使用hash值排序，所以打印出来是无序的
B={j*j for j in range(2,30,2)}
print(B)