"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

link：https://leetcode-cn.com/problems/divide-two-integers
"""


def divide1(dividend, divisor):
    """
    运行没有出现问题，但是时间复杂度超出了限制
    :param dividend:
    :param divisor:
    :return:
    """
    flag = True  # 是否为同号
    if (dividend >= 0 > divisor) or (divisor >= 0 > dividend):
        flag = False
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = -divisor
    temp, res = divisor, 0
    while temp <= dividend:
        temp += divisor
        res += 1
    return res if flag else -res


def divide2(dividend: int, divisor: int) -> int:
    """
    这个算法的思路就是将 除数成倍的增长，通过<<(左移)运算符，当增长到大于被除数时用被除数减去最接近被除数的数，然后重复上面步骤最后求出她的商
    link:https://leetcode-cn.com/problems/divide-two-integers/solution/kuai-su-qiu-jie-di-gui-ci-shu-zhi-shu-di-jian-shan/
    :param dividend:
    :param divisor:
    :return:
    """
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        tag = 1
    else:
        tag = -1
    res = divCreas(abs(dividend), abs(divisor))
    if tag == -1: res = 0 - res
    if res > (2 << 30) - 1:
        return (2 << 30) - 1
    elif res < 0 - (2 << 30):
        return 0 - (2 << 30)
    return res


def divCreas(dividend: int, divisor: int) -> int:
    ex, count = divisor, 0
    t, m = 0, 1
    if dividend < divisor:
        return 0
    while dividend - t - ex >= 0:
        t += ex
        count += m
        m += m
        ex += ex
    if dividend - t > 0:
        return count + divCreas(dividend - t, divisor)
    return count


print(divide2(44, 3))
