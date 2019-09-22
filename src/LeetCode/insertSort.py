"""
插入排序
"""


def inserSort(nums):
    size = len(nums)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp
    return nums


print(inserSort([5, 10, 13, 14, 3, 1, 2, 7, 11, 8, 12, -1]))


