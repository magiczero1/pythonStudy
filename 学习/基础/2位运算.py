#0b00000100  == 4
#0o00001000  == 8

print(4&8)   #对位有一个0，则都是0. 位与运算
print(4|8)   #对位有一个1，则都是1. 位或运算
print(4<<1)  #将0b00000100变为0b00001000左移1位，相当于*2
print(4>>2)  #将0b00000100变为0b00000010右移2位，相当于/2

print(4^8)   # ^ 按位异运算 两者相同则都变为0，两者不同则变为1.
print(bin(13))
print(bin(4))
print(13^4)
print(4^13)
#---------------------------------
print(bin(4))
print(~4)  # ~反转运算，将二进制数4加1后，取相反数
print(~199)