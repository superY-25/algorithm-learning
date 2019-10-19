"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

link：https://leetcode-cn.com/problems/combination-sum
"""


def combinationSum(candidates: list, target: int) -> list:
    """
    动态规划
    :param candidates:
    :param target:
    :return:
    """
    dic = {}
    for i in range(1, target + 1):
        dic[i] = []

    for i in range(1, target + 1):
        for j in candidates:
            if i == j:
                dic[i].append([i])
            elif i > j:
                for k in dic[i - j]:
                    x = k[:]
                    x.append(j)
                    x.sort()  # 升序，便于后续去重
                    if x not in dic[i]:
                        dic[i].append(x)

    return dic[target]


print(combinationSum([2,3,6,7], 7))