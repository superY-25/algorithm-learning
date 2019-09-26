
"""
动态规划问题：
动态规划遵循一套固定的流程：递归的暴力解法 -> 带备忘录的递归解法 -> 非递归的动态规划解法
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

link：https://leetcode-cn.com/problems/coin-change

"""


def fib1(n):
    if n is 1 or n is 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print(fib1(9))
"""
递归问题的时间复杂度计算：子问题的个数 * 子问题需要的时间
斐波那契数列的递归解法的时间复杂度O(2^n)
"""

# 动态规划的第一个性质：重叠子问题


def helper(memo, n):
    if n is 1 or n is 2:
        return 1
    if memo.get(n) is not None:
        return memo[n]
    else:
        memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
    return memo[n]


def fib2(n):
    if n < 0:
        return 0
    memo = {}
    return helper(memo, n)

"""
空间换时间 O(n)
"""
print(fib2(9))


def fib3(n):
    dp = {1: 1, 2: 1}
    if n == 1 or n == 2:
        return dp[n]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


"""
空间换时间 O(n), 但是可以改进
"""
print(fib3(9))


def fib4(n):
    if n == 1 or n == 2:
        return 1
    pre, curr = 1, 1
    for i in range(3, n + 1):
        ret = pre + curr
        pre = curr
        curr = ret
    return ret


print(fib4(9))


def coinchange(coins, amount):
    res = [0 for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        cost = float('inf')
        for c in coins:
            if i - c >= 0:
                cost = min(cost, res[i - c] + 1)
        res[i] = cost

    if res[amount] == float('inf'):
        return -1
    else:
        return res[amount]


print(coinchange([1, 2, 5], 11))
