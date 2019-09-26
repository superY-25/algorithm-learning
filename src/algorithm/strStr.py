"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1

link：https://leetcode-cn.com/problems/implement-strstr
"""


def strStr(haystack: str, needle: str) -> int:
    """
    此算法是取巧算法，运用编程语言的特性进行求解
    :param haystack:
    :param needle:
    :return:
    """
    haystack_len = len(haystack)
    needle_len = len(needle)
    curr = -1
    for i in range(haystack_len - needle_len + 1):
        if haystack[i: i + needle_len] == needle:
            curr = i
            break
    return curr

def strStr(haystack: str, needle: str) -> int:
    """
    通过循环str来匹配字符串，
    :param haystack:
    :param needle:
    :return:
    """


print(strStr("mississippi", "issip"))
