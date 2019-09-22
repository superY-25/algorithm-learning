"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

link：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


def removeDuplicates(nums):
    size = len(nums)
    j = 0
    for i in range(1, size):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1


print(removeDuplicates([1,1,2]))