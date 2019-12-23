"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""


def myPow(x: float, n: int):
    """
    暴力解法 超时
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n > 0:
        s = x
        for _ in range(1, n):
            s = s * x
        return s
    elif n < 0:
        s = x
        for _ in range(1, -n):
            s = s * x
        return 1 / s


def myPow1(x: float, n: int):
    pass