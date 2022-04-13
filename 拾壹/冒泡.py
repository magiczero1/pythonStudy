#冒泡排序
import random as r

List = [76, 246, 815, 968, 773, 813, 509, 954, 54, 341]

def bubbleSort(list1):
    n = len(list1)
    for j in range(n):
        for i in range(n-1,j-1,-1):
            if list1[i] > list1[i-1]:
                list1[i],list1[i-1] = list1[i-1],list1[i]
    return list1

print(bubbleSort(List))

def selectSort(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        positionOfmax = 0
        for j in range(1,i+1):
            if alist[j] < alist[positionOfmax]:
                positionOfmax = j
        temp = alist[i]
        alist[i] = alist[positionOfmax]
        alist[positionOfmax] = temp
    return alist

print(selectSort(List))




