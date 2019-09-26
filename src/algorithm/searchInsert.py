"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""


def searchInsert(nums, target):
    """
    整个遍历数组，O(n)
    :param nums:
    :param target:
    :return:
    """
    nums_len = len(nums)
    for i in range(nums_len):
        if nums[i] >= target:
            return i
    return nums_len


def searchInsert1(nums, target):
    nums_len = len(nums)
    lo, hi = 0, nums_len
    while lo <= hi:
        mid = ((hi - lo) // 2) + lo
        if mid == nums_len or nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
    return lo


print(searchInsert1([1,3,5,6], 7))
