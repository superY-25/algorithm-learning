
"""
选择排序:
"""


def selectSort(nums):
    size = len(nums)
    for i in range(size - 1):
        index = i
        for j in range(i+1, size):
            if nums[index] > nums[j]:
                index = j
        if i is not index:
            temp = nums[i]
            nums[i] = nums[index]
            nums[index] = temp
    return nums


print(selectSort([5, 10, 13, 14, 3, 9, 0, 6, 4, 1, 2, 7, 11, 8, 12]))


