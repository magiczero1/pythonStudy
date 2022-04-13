#.sort不改变列表id
s=[1,2,3,5,121,231,4231,412]
s.sort() #默认升序排序
print(s)
s.sort(reverse=False)
print(s) #
s.sort(reverse=1)#当reverse=true时，为降序排序
print(s) #
#sorted重新创建一个列表
a=sorted(s)
print(a)
a=sorted(s,reverse=1)
print(a)