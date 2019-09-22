
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
"""

def maxSubArray(nums):
    """
    暴力循环之data-reuse算法
    :param nums:
    :return:
    """
    res = nums[0]
    nums_len = len(nums)
    for i in range(nums_len):
        sum = 0
        j = i
        while j < nums_len:
            sum = sum + nums[j]
            res = max(sum, res)
            j += 1
        else:
            res = max(sum, res)
    return res


def maxSubArray1(nums):
    """
    动态规划
    :param nums:
    :return:
    """
    maxSum, rSum = nums[0], 0
    for n in nums:
        rSum = rSum + n
        maxSum = max(maxSum, rSum)
        rSum = max(rSum, 0)
    return maxSum


print(maxSubArray1([-1,0,-2]))




