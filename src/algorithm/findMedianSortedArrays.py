"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

link：https://leetcode-cn.com/problems/median-of-two-sorted-arrays

"""


def findMedianSortedArrays(nums1, nums2):
    """
    寻找两个有序数组的中位数，此算法主要是求中位数的数学算法
    :param nums1:
    :param nums2:
    :return:
    """
    n = nums1 + nums2
    n.sort()
    s = len(n)
    if s % 2 == 0:
        return (n[s // 2 - 1] + n[s // 2])/2.0
    else:
        return n[s // 2] / 1.0


print(findMedianSortedArrays([1, 2], [3, 4, 5]))
