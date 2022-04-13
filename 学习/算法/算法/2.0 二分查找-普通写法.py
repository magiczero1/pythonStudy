#二分查找是基于有序数据的前提【分治策略的体现】

#以下程序是基于上大下小的数据排序实现的算法
def binarySearch(alist,item):
    up = len(alist)-1
    down = 0
    found = False
    while down <= up and not found:
        mid = (up + down ) // 2
        if alist[mid] < item:
            down = mid + 1
        elif alist[mid] > item:
            up = mid - 1
        else:
            found = True
    return found

