#数据具有线性关系，可以通过下标直接访问，则可以使用顺序查找
#O(n)    最好的情况是1次，最坏的次数是n次

def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return pos

listDemo = [0, 1, 2, 3, 4, 5, 6, 8, 9]
print(sequentialSearch(listDemo,3))