
def mySqrt(x: int) -> int:
    """
    暴力破解 时间超出限制
    :param x:
    :return:
    """
    if x == 0 or x == 1:
        return x

    for i in range(1, x // 2 + 2):
        if i ** 2 == x:
            return i
        elif i ** 2 > x:
            return i - 1


def mySqrt1(x: int) -> int:
    """
    二分法
    :param x:
    :return:
    """
    if x == 0 or x == 1:
        return x
    lo, hi = 0, x // 2
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # 注意这里的中位数取值
        if mid ** 2 > x:
            hi = mid - 1
        else:
            lo = mid
    return lo


for i in range(20):
    print(str(i)+"的开根号=", mySqrt1(i))
