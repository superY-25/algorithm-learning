"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
"""


def minCostClimbingStairs(cost):
    cost_len = len(cost)
    if cost_len == 0 or cost_len == 1:
        return 0
    cost1 = 0
    cost2 = min(cost[0], cost[1])
    for i in range(2, cost_len):
        temp = min((cost[i] + cost2), (cost[i - 1] + cost1))
        cost1 = cost2
        cost2 = temp
    return cost2


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))
