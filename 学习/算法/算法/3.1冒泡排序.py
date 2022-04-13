import random
list1 = [68225, 4670, 18680, 35712, 13750, 94995, 45514, 22626, 6200, 52687]
#生成一个列表
'''
for i in range(10):
    x = random.randint(1, 100000)
    list1.append(x)
'''

#冒泡排序第一次排序，是针对最大项或者最小项进行排序。
#复杂度O(n²)   ①不需要额外空间的开销（相邻数据项的空间可以忽略）②可适应链表
def bublleSort(alist):
    k = 0
    for passnum in range(len(alist)-1,0,-1):  #外层：每循环一次，就将该循环组中的最大值排到末尾
        for i in range(passnum):   #内层：两两比对，并决定是否交换
            k += 1
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            print("比对了{0}次".format(k))

listDemo = [1,22,3,4,12,31,3,13,414,4412,12,45]
bublleSort(listDemo)
print(listDemo)

#冒泡排序的性能改进  ： 增加一个检测有无排序操作的检测点。
def shortBubbleSort(alist):
    exchange = True #交换监测点
    passnum = len(alist)-1

    while passnum > 0 and exchange :
        exchange = False    #逆向思维进入循环后立马变为False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]  #交换写法，仅限python
                exchange = True
        passnum -= 1
