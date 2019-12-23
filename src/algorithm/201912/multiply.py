"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

"""


def multiply(num1: str, num2: str):
    """
    暴力破解
    :param num1:
    :param num2:
    :return:
    """
    if num1 == 0 or num2 == 0:
        return '0'
    ret = '0'
    k = 0
    for i in reversed(num1):
        pre = 0
        cur = ''
        for j in reversed(num2):
            s = int(i) * int(j) + pre
            pre = s // 10
            cur = cur + str(s % 10)
        if pre != 0:
            cur = cur + str(pre)
        ret = addnumber(ret, '0' * k + cur)
        k += 1
    return ret[::-1]


def addnumber(num1: str, num2: str):
    pre = 0
    i, j = 0, 0
    num1
    num2
    ret = ''
    while i < len(num1) and j < len(num2):
        s = int(num1[i]) + int(num2[j]) + pre
        ret = ret + str(s % 10)
        pre = s // 10
        i += 1
        j += 1
    if i < len(num1):
        while i < len(num1):
            s = int(num1[i]) + pre
            ret = ret + str(s % 10)
            pre = s // 10
            i += 1
    elif j < len(num2):
        while j < len(num2):
            s = int(num2[j]) + pre
            ret = ret + str(s % 10)
            pre = s // 10
            j += 1
    if pre != 0:
        ret = ret + str(pre)
    return ret


if __name__ == '__main__':
    num1 = "103"
    num2 = "98"
    print(multiply(num1, num2))
    # print('0' * 2)


