"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        动态规划，只要当天比前一天贵，能收益就卖掉。
        :param prices:
        :return:
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,6,4,3,1]))