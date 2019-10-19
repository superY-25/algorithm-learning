"""
快速排序
"""


def quickSort(nums, s, r):
    if s < r:
        pivot = partition(nums, s, r)
        quickSort(nums, s, pivot - 1)
        quickSort(nums, pivot + 1, r)


def partition(nums, s, r):
    pivot = nums[r]
    i, j = s - 1, s
    while j < r:
        if nums[j] > pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    nums[i+1], nums[r] = nums[r], nums[i + 1]
    print(nums)
    return i + 1


quickSort([2, 13, 8, 4, 2, 7, -1], 0, 6)