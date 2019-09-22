"""
罗马数字转整数
"""


def romanToInt(roman):
    romans = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
              'V': 5, 'IV': 4, 'I': 1}
    res = 0
    i = 0
    while i < (len(roman) - 1):
        i += 1
        if romans[roman[i - 1]] < romans[roman[i]]:
            res -= romans[roman[i - 1]]
        else:
            res += romans[roman[i - 1]]
    res += romans[roman[i]]
    return res


print(romanToInt('IX'))
