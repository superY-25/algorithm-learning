

def permute(nums):
    if not nums:
        return [[]]
    pre = [[nums[0]]]
    for i in range(1, len(nums)):
        cur = []
        for item1 in pre:
            for j in range(i + 1):
                item2 = item1.copy()
                item2.insert(j, nums[i])
                cur.append(item2)
        pre = cur
    return pre


if __name__ == '__main__':
    print(permute([1,2,3]))
