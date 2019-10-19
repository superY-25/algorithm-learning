
"""
堆的例子：维护堆的性质（最大堆：所有的父节点要大于孩子节点，最小堆：所有的父节点要小于孩子节点）
"""


def max_heapify(nums, i):
    """
    维持堆的特性，使用递归的方法
    :param nums:
    :param i:
    :return:
    """
    l = left(i)
    r = right(i)
    i -= 1
    if l <= len(nums) and nums[i] < nums[l]:
        maximun = l
    else:maximun = i
    if r <= len(nums) and nums[maximun] < nums[r]:
        maximun = r
    if maximun != i:
        nums[maximun], nums[i] = nums[i], nums[maximun]
        max_heapify(nums, maximun + 1)


def max_heapify1(nums, i):
    """
    维持堆的特性，使用非递归的方法
    :param nums:
    :param i:
    :return:
    """
    while True:
        l = left(i)
        if l > len(nums):
            break
        r = right(i)
        i -= 1
        if l <= len(nums) and nums[i] < nums[l]:
            maximun = l
        else:
            maximun = i
        if r <= len(nums) and nums[maximun] < nums[r]:
            maximun = r
        if maximun != i:
            nums[maximun], nums[i] = nums[i], nums[maximun]
            i = maximun + 1
        else:
            break

def left(i):
    return 2 * i - 1


def right(i):
    return 2 * i


A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
max_heapify1(A, 2)
print(A)
