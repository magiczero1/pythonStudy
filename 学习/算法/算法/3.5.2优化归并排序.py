def mergeSort2(alist):
    #递归结束条件
    if len(alist) <= 1:
        return alist

    #分解问题，调用递归
    mid = len(alist)//2
    left = mergeSort2(alist[:mid])
    right = mergeSort2(alist[mid:])

    #左右归并
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

demoList = [4,5,1,1,45,6,123,5,7]
print(mergeSort2(demoList))