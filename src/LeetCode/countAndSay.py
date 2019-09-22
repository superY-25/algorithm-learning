"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

link：https://leetcode-cn.com/problems/count-and-say
"""


def countAndSay(n: int) -> str:
    """
    独立思考出的结果
    :param n:
    :return:
    """
    curr = '1'
    for i in range(2, n+1):
        temp = curr + '0'
        curr = ''
        count = 1
        for j in range(1, len(temp)):
            if temp[j] != temp[j - 1]:
                curr += str(count) + temp[j - 1]
                count = 1
            else:
                count += 1
    return curr


def countAndSay1(n: int) -> str:
    """
    groupby的用法
    :param n:
    :return:
    """
    from itertools import groupby
    result = '1'
    for i in range(1, n):
        result = ''.join([str(len(list(g))) + k for k, g in groupby(result)])
    return result


print(countAndSay(5))

print(countAndSay1(5))

from itertools import groupby
print(list(groupby('111221')))
for k, g in groupby('111221'):
    print('k=', k, 'g=', list(g))

