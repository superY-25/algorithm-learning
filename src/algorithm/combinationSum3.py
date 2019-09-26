"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
"""


def combinationSum3(k, n):
    for i in range(1, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                if i + j + k == n:
                    list.append([i, j, k])
    return list


print(combinationSum3(3, 9))
