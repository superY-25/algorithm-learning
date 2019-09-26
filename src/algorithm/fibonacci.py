"""
斐波那契数列的多种实现方法
"""


def fibonacci1(n):
    """
    递归实现
    :param n:
    :return:
    """
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


def fibonacci2(n):
    """
    迭代法实现 时间复杂度O(n),空间复杂度O(n)
    :param n:
    :return:
    """
    if n < 0:
        return -1
    temp = [i for i in range(n + 1)]
    i = 2
    while i <= n:
        temp[i] = temp[i - 1] + temp[i - 2]
        i += 1
    return temp[n]


def fibonacci3(n):
    """
    迭代法的优化，时间复杂度O(n)，使得空间复杂度降到O(1)
    迭代时每次记录前两个数的值，当前值等于前两个值的和
    :param n:
    :return:
    """
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    c = 2
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


def fibonacci4(n):
    """
    通项公式法和快速幂算法(并不知道为什么要这么做)
    :param n:
    :return:
    """
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]
    for i in range(2, n + 1):
        multiply(F, M)


if __name__ == '__main__':
    print(fibonacci4(70000))

