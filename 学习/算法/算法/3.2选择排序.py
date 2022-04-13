#选择排序实现的原理与冒泡类似
#区别在于：选择排序是先找到列表中的最大值，然后与列表中的最后一项进行交换。重复操作。

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):             #找当前循环组中最大值的位置
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]                           #将当前循环组的末尾值放进临时变量保存
        alist[fillslot] = alist[positionOfMax]           #将末尾更新未最大值
        alist[positionOfMax] = temp                      #将原位置更新为临时变量里的值

demoList = [1,2,223,231313,7,8991,314]
selectionSort(demoList)
print(demoList)