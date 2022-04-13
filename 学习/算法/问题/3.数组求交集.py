#'''第一种解法，遍历求解'''
nums1 = [4,9,5,34,5,2,42,3,2,5352,62,23,4,24,2,1,23,131,4,5,5,62,24,]
nums2 = [9,4,9,8,4,123,12,314,1,231,5,12,3,13,13,1,12,31,12,312,3]
conum = set()#创建空集只能用set
for i in range(len(nums2)):
    if nums2[i] in nums1:
        conum.add(nums2[i])
conum = list(conum)
print(conum)
#算法空间复杂度O(1)，时间复杂度O(1)
'''第二种解法，求交集'''
nums2_set = set(nums2)
nums1_set = set(nums1)
print(nums1_set & nums2_set )