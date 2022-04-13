#二分查找是基于有序数据的前提【分治策略的体现】

#以下程序是基于上大下小的数据排序实现的算法
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:
                return binarySearch(alist[mid+1:],item)   #更新左边界
            else:
                return binarySearch(alist[:mid],item)      #更新右边界

print(binarySearch([0,2,4,5,6,7,9],13))