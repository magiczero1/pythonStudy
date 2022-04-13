#mergeSort  将原表不断分裂为两半，然后对两半分别进行归并排序。
#归并排序的核心是递归，复杂度O(nlogn)

def mergeSort(alist):
    if len(alist) > 1:     #基本结束条件，元素个数为1的时候不进行分裂
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf): #拉链式交错，把左右半部从小到大并到结果列表中
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):   #归并左半部分剩余项
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):   #归并右半部分剩余项
            alist[k] = righthalf[j]
            j = j+1
            k = k+1

a = [1,2,3,4,8,6,3,9,0]
mergeSort(a)
print(a)