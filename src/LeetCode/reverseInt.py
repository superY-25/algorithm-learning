
"""
一个32位有符号整数 将其反转，若溢出则返回0
溢出  -2^31 ~ 2^31-1
"""


def reverseInt(num: int) -> int:
    if num is 0:
        return 0
    temp = str(num)
    s = ''
    if temp[0] is '-':
        s = '-'
    s += temp[len(temp) - 1::-1].rstrip('-').lstrip('0')
    num = int(s)
    if -2**31 <= num <= 2**31 - 1:
        return num
    return 0


print(reverseInt(-1120))


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    s = str(x)
    newstr = ''
    if s[0] == '-':
        newstr = '-'
    newstr += s[len(s) - 1::-1].lstrip('0').rstrip('-')
    x = int(newstr)
    if 2 ** 31 - 1 >= x >= -2 ** 31:
        return x
    else:
        return 0


print(reverse(-1120))


a = '1234'
b = a[3::-2]
print(b)

