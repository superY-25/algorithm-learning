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

def myPow1(x: float, n: int):
    """
    递归计算(二分法)
    when x == 0 or x == 1，return x
    when n == 0，return 1
    when n < 0，return 1 / myPow1(x, -(n + 1)) / x
    when n % 2 == 1 return myPow1(x * x, n / 2) * x
    when n % 2 == 0 return myPow1(x * x, n /2)
    :param x:
    :param n:
    :return:
    """
    if x == 0 or x == 1:
        return x
    elif n == 0:
        return 1
    elif n < 0:
        return 1 / myPow1(x, -(n + 1)) / x
    elif n % 2 == 1:
        return myPow1(x * x, n // 2) * x
    elif n % 2 == 0:
        return myPow1(x * x, n // 2)


if __name__ == '__main__':
    print(myPow1(2, 5))
    # for i in range(2, 10, 2):
    #     print(i)