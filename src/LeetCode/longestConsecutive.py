"""
最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。
link：https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""


def longestConsecutive(nums):
    """
    算法正确，算法时间复杂度为O(n^2)但不符合O(n)的时间复杂度要求
    :param nums:
    :return:
    """
    res = []
    max_len = 0
    for n in nums:
        if n in res:
            continue
        else:
            s = n
            cur = s + 1
            res.append(n)
            while cur in nums:
                if cur not in res:
                    res.append(cur)
                cur += 1
            max_len = max(max_len, cur - s)
    return max_len


def longestConsecutive2(nums):
    """
    在Leecode测试通过，排序算法的时间复杂度应该在O(nlgn)。
    :param nums:
    :return:
    """
    size = len(nums)
    if size == 0:
        return 0
    nums.sort()
    s = nums[0]
    cur = nums[0]
    max_len = 1
    for i in range(1, size):
        if nums[i - 1] + 1 == nums[i] or nums[i - 1] == nums[i]:
            cur = nums[i]
        else:
            s = nums[i]
        max_len = max(max_len, cur - s + 1)
    return max_len


def longestConsecutive3(nums):
    """

    :param nums:
    :return:
    """
    newnums = list(set(nums))
    size = len(newnums)
    if size == 0:
        return 0
    max_len = 0
    for n in newnums:
        if n - 1 not in newnums:
            cur = n
            cur_len = 1
            while cur+1 in newnums:
                cur += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
    return max_len


print(longestConsecutive3([100, 1, 200, 4, 3, 2]))

