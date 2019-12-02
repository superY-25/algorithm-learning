"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
"""


class NumArray:
    """
    常规的从i——j的累加求和
    """

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        s = 0
        for k in range(i, j + 1):
            s += self.nums[i]
        return s


class NumArray1:

    def __init__(self, nums):
        self.nums = nums
        self.sums = [0]
        for i in range(len(nums)):
            self.nums[i + 1] = self.nums[i] + nums[i]

    def sumRange(self, i, j) -> int:
        return self.nums[j + 1] - self.nums[i]
