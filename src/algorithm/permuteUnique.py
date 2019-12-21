"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
"""
def permuteUnique(nums):
    if not nums:
        return [[]]
    pre = [[nums[0]]]
    for i in range(1, len(nums)):
        cur = []
        for item1 in pre:
            for j in range(i + 1):
                item2 = item1.copy()
                item2.insert(j, nums[i])
                if item2 not in cur:
                    cur.append(item2)
        pre = cur
    return pre


if __name__ == '__main__':
    print(permuteUnique([1, 2, 1]))
