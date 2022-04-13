s1={10,20,30,50}
s2={50,20,30,10}
print(s1==s1)
#issubset()子集
s3={10,20,30,50,200,21,12,1,2}
print(s2.issubset(s3))#s2是s3的子集
#issuperset()超集
print(s3.issuperset(s2))#s2是s3的超集
#isdisjoint() 无交集
print(s3.isdisjoint(s2))  #有交集显示为false
#intersection()和& 求交集
s5=s2.intersection(s3)
s6=s2&s3
print(s5)
print(s6)
#union()     |  求并集
a={2,21,231,4,2131}
b={4,3123.412,21}
c=a.union(b)
d=a|b
print(c)
print(d)
#difference() 求差集,保留前者不一样的。
e=a.difference(b)#e=a-b
f=b.difference(a)#f=b-a
print(e)
print(f)
#symmetric_difference()   ^ 对称差集,保留二者不一样的
g=a.symmetric_difference(b)
h=a^b
print(g)
print(h)