"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
"""


def removeElement(nums, val):
    """
    双指针法
    :param nums:
    :param val:
    :return:
    """
    i, j = 0, 0
    while i < len(nums):
        if nums[i] == val:
            i += 1
        else:
            if i != j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i += 1
            j += 1
    return j


print(removeElement([3,2,2,3], 3))
