#quickSort 取首位充当"中位值"
def quickSort(alist):
    midvalue = alist[0]
    leftmark = 1
    rightmark = len(alist)-1

    while leftmark < rightmark:
        if alist[leftmark] > midvalue:
            rightmark -= 1
            if alist[leftmark] < alist[rightmark]:
                alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
                leftmark += 1
        else:
            leftmark += 1

    return alist

print(quickSort([1,3,2,4,7,111,3,45,6,7,2,424]))