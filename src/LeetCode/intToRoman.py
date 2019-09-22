"""
整数转罗马数字
贪心算法
"""


def intToRoman1(num):
    romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for key, value in romans.items():
        while num >= key:
            res += value
            num -= key
    return res


print(intToRoman1(3))
