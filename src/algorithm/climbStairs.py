
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


def climbStairs(n):
    res = 0
    a, b = 0, 1
    for i in range(1, n+1):
        res = a + b
        a = b
        b = res
    return res


print(climbStairs(2))

