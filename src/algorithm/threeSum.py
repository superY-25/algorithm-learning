"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
未理解
link：https://leetcode-cn.com/problems/3sum

"""


def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        # 排好序之后，如果nums[i]>0，说明后面的数全部大于0
        if nums[i] > 0:
            break
        if i == 0 or nums[i] > nums[i - 1]:  # 去重
            left, right = i + 1, len(nums) - 1
            # 剪枝
            if nums[i] + nums[left] + nums[left + 1] > 0 or nums[i] + nums[right - 1] + nums[right] < 0:
                continue
            while left < right:
                ident = nums[i] + nums[left] + nums[right]
                if ident == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif ident < 0:
                    left += 1
                else:
                    right -= 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
