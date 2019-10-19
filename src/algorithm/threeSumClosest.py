"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案

link：https://leetcode-cn.com/problems/3sum-closest
"""


def threeSumClosest(nums, target):
    """
    暴力求解
    :param nums:
    :param target:
    :return:
    """
    res = nums[0] + nums[1] + nums[2]
    size = len(nums)
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                dv1 = abs(res - target)
                dv2 = abs((nums[i] + nums[j] + nums[k]) - target)
                if dv2 < dv1:
                    res = nums[i] + nums[j] + nums[k]
    return res


def threeSumClosest2(nums, target):
    """
    排序+双指针法
    算法思路：
    :param nums:
    :param target:
    :return:
    """
    nums.sort()
    res = target
    dv = 2 ** 31
    for k in range(len(nums) - 2):
        i, j = k + 1, len(nums) - 1
        while i < j:
            res_new = nums[k] + nums[i] + nums[j]
            if res_new == target:
                return target
            elif res_new < target:
                if target - res_new < dv:
                    res = res_new
                    dv = target - res_new
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            else:
                if res_new - target < dv:
                    res = res_new
                    dv = res_new - target
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


if __name__ == '__main__':
    print(threeSumClosest2([-1, 2, 1, 0], 1))
