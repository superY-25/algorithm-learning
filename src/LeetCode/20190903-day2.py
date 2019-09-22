"""
两个算法：1、将数字开头的字符串转换成数字。比如："4193 with words" -> 4193
        2、判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
"""
import re


def myAtoi(s):
    """
    使用正则表达式:奇思淫计
    :param str:
    :return:
    """
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


print(myAtoi("-91283472332"))


def myatoi1(s):
    """
    普通思路：判断字符串中的每一个字符是否是数字
    :param str:
    :return:
    """
    s = s.lstrip()
    if s == '':
        return 0
    i = 0
    if s[0] == '-' or s[0] == '+':
        i = 1

    while i < len(s):
        try:
            int(s[i])
        except:
            break
        i += 1
    s = s[:i]
    if s == '' or s == '-' or s == '+':
        return 0
    num = int(s)
    if num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if num < -2**31:
        return -2 ** 31
    return num


print(myatoi1("words and 987"))


"""
给出一个整数，判断是否是回文数。
"""

def isPalindrome(num):
    """
    最简单粗暴的算法：将整数全部颠倒，比较原来的数和新生成的数是否相等
    :param num:
    :return:
    """
    s = str(num)
    news = s[len(s) - 1::-1]
    if s == news:
        return True
    else:
        return False


print(isPalindrome(121))

