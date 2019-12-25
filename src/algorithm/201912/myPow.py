"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""


def myPow(x: float, n: int):
    """
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n > 0:
        s = x
        for i in range(0, n, 2):
            s = s ** 2
        for j in range(n - i):
            s = s * x
        return s
    elif n < 0:
        s = x
        i = 1
        for i in range(0, -n, 2):
            s = s ** 2
        for j in range(-n - i):
            s = s * x
        return 1 / s


if __name__ == '__main__':
    print(myPow(2, 5))
    # for i in range(2, 10, 2):
    #     print(i)