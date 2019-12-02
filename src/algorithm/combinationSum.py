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
            if i == j and [i] not in dic[i]:
                dic[i].append([i])
            elif i > j:
                for k in dic[i - j]:
                    x = k[:]
                    x.append(j)
                    x.sort()  # 升序，便于后续去重
                    if x not in dic[i]:
                        dic[i].append(x)
    return dic[target]


if __name__ == '__main__':
    print(combinationSum([10,1,2,7,6,1,5], 8))
    # a = [[1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 2],
    #      [1, 1, 1, 3],
    #      [1, 1, 2, 2],
    #      [1, 1, 4],
    #      [1, 2, 3],
    #      [1, 5],
    #      [2, 2, 2],
    #      [2, 4],
    #      [3, 3],
    #      [6]]
    # b = [2,5,7,8,12,15]
    # for i in a:
    #     s = 0
    #     for j in i:
    #         s += b[j-1]
    #     print(str(i) + ' = ', s)







