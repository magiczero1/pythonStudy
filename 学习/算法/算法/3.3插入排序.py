#类似于整理手牌，需要额外的空间(由抽取的数据来腾出空间)
#复杂度O(n²)

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentValue = alist[index]   #抽取对比的数据
        position = index

        while position > 0 and alist[position - 1] > currentValue:  #对比，如果抽取的数据小于当前数据，则把当前数据往后移动。
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue    #将抽取的数据放在正确的位置
    return alist

a = [1,3,5,2,6]

print(insertionSort(a))
