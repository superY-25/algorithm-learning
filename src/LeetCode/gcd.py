"""
最大公约数算法：
1、欧几里得法：两个非负整数p和q的最大公约数，若q=0则最大公约数为p。
             否则将p除以q得到余数r，则p和q的最大公约数就是q和r的最大公约数
2、数学定义法：通过两个数的公共因子，直到没有公共因子，最后将所有的公共因子求积。
"""


def gcd(a, b):
    """
    欧几里得算法--递归
    :param a:
    :param b:
    :return:
    """
    if a == 0:
        return b
    if b == 0:
        return a
    c = (a % b if a > b else b % a)
    d = a if a < b else b
    return gcd(c, d)


def gcd1(a: int, b: int) -> int:
    """
    欧几里得算法--非递归
    :param a:
    :param b:
    :return:
    """
    c = a if a >= b else b
    d = a if a < b else b
    while c != 0 and d != 0:
        c = d
        d = c % d


print(gcd(8, 12))
