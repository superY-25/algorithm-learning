"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

link：https://leetcode-cn.com/problems/two-sum
"""


def twoSum(nums, target):
    """
    空间换时间, 时间复杂度O(n),空间复杂度O(n)
    :param nums:
    :param target:
    :return:
    """
    temp = {}
    for index, val in enumerate(nums):
        diff = target - val
        if diff in temp:
            return [temp[diff], index]
        else:
            temp[val] = index
    return None


def twoSum1(nums, target):
    """
    找出数组中两个数之和为target的所有不重复组合
    :param nums:
    :param target:
    :return:
    """
    temp = []
    ret = []
    for index, value in enumerate(nums):
        diff = target - value
        if diff in temp:
            ret.append([diff, value])
        else:
            temp.append(value)
    return ret


print(twoSum1([2, 7, 11, 15, 16], 18))
