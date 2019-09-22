"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

link：https://leetcode-cn.com/problems/merge-sorted-array
"""


def merge(nums1,m,nums2,n):
    i, j = 0, 0
    while i < m + j and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            for k in range(m + j, i, -1):
                nums1[k] = nums1[k - 1]
            nums1[i] = nums2[j]
            j += 1
            i += 1
    if j < n:
        for m in range(i, m+n):
            nums1[m] = nums2[j]
            j += 1


nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
merge(nums1, 1, nums2, 5)
print(nums1)
