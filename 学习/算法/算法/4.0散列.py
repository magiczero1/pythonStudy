#Hashing 复杂度O(1)
#hash table(散列表/哈希表)  其中每一个项被称为槽（slot）一般情况将槽数设置为质数
import random
list = [18, 67, 96, 58, 49, 42, 11, 15, 36, 45]
'''for i in range(10):
    num = random.randint(1,100)
    list.append(num)
print(list)'''
#"求余数"用于散列表中查找   即值对槽数求余，然后把对应值放入槽中。
#如有一个槽数为99的哈希表，有以上list数值。则可将每个数值取出来对槽数求余，即可得到。(此时有致命缺陷，倍数会被覆盖掉)
#准完美散列函数：①冲突尽量少 ②计算 难度低 ③节约空间
#用途1：作为"指纹"-密码，①压缩性  ②易计算性 ③抗修改性 ④ 抗冲突性     如MD5、S(secure)H(hash)A(algrithem)
#用途2：一致性校验。①软件是否重复下载 ②软件是否被篡改 ③相同文件无需存储多次
#用途3：区块链：分布式数据库。区块：head+body
hashtable = [None]*18
i = 0
while i < len(list):
    index = list[i]%18
    hashtable[index] = list[i]
    i += 1

print(hashtable)

