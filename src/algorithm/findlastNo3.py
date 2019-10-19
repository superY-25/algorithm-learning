"""
找到数组中第三小的数
"""


def findlastNo3(nums):
    one, two, three = max(nums), max(nums), max(nums)
    for i in range(len(nums)):
        if nums[i] < one:
            three = two
            two = one
            one = nums[i]
        elif nums[i] < two:
            three = two
            two = nums[i]
        elif nums[i] < three:
            three = nums[i]
    return three


print(findlastNo3([-2, -3, 4, -1, 1, 2, 8, 5, 3, 0, -4]))
