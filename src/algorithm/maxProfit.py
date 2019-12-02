"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""


def maxProfit1(prices):
    """
    暴力循环  超时
    :param prices:
    :return:
    """
    maxprofit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            cur = prices[j] - prices[i]
            if cur > maxprofit:
                maxprofit = cur
    return maxprofit


def maxProfit(prices):
    """
    动态规划
    :param prices:
    :return:
    """
    i = 0
    maxp = 0
    for j in range(1, len(prices)):
        cur = prices[j] - prices[i]
        if cur < 0:
            i = j
        elif cur > maxp:
            maxp = cur
    return maxp


if __name__ == '__main__':
    print(maxProfit1([7,1,5,3,6,4]))
    print(maxProfit([7, 1, 5, 3, 6, 4]))


