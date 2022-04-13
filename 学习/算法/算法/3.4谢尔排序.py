#ShellSort 以插入排序为基础，对无序表划分子列表进行插排，让无序表尽可能接近有序
#复杂度O(n的二分之三次方)

def shellSrot(alist):
    sublistcount = len(alist)//2   # 初始化子列表间隔

    while sublistcount > 0:
        for startposition in range(sublistcount):    #对子列表排序
            gapInertionSort(alist,startposition,sublistcount)
        print("After increment of size",sublistcount,"The list is",alist)
        sublistcount = sublistcount // 2

def gapInertionSort(alist,start,gap):      #变形的子列表插排
    for i in range(start + gap,len(alist),gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentValue
