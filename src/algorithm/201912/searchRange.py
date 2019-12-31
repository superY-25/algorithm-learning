"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""


def searchRange(nums: list, target: int):
    if not nums:
        return [-1, -1]
    return handle(nums, target, 0, len(nums)-1)


def handle(nums: list, target: int, l: int, h: int) -> list:
    mid = (l + h) // 2
    if mid >= len(nums) or mid < 0 or l > h:
        return [-1, -1]
    if nums[mid] == target:
        low = mid - 1
        while low >= l and nums[low] == target:
            low = low - 1
        hig = mid + 1
        while hig < len(nums) and nums[hig] == target:
            hig = hig + 1
        return [low + 1, hig - 1]
    if nums[mid] > target and l <= (mid - 1):
        return handle(nums, target, l, mid - 1)
    elif nums[mid] < target:
        return handle(nums, target, mid + 1, h)
    else:
        return [-1, -1]


if __name__ == '__main__':
    nums = [1,2,2, 3]
    target = 2
    print(searchRange(nums, target))
