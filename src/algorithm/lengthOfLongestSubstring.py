"""
无重复字符串的最长子串长度
题目：给定一个字符串，找出其中不含重复字符的最长子串的长度
示例1： 输入 "abcabcbb"  输出 3  解释  因为无重复字符的最长子串是"abc"，所以其长度为3
示例2： 输入 "bbbb"  输出  1  解释  因为无重复字符的最长子串是"b"，所以其长度为1
示例3： 输入 "pwwkew" 输出  3  解释  因为无重复字符的最长子串是"wke" 所以其长度为3 请注意，答案必须是子串的长度，"pwke"并不是字符串的子串

link：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


def lengthOfLongestSubstring(s):
    """
    最长子串的长度
    :param s:
    :return:
    """
    res = ''
    n = 0
    j = 0
    while j < len(s):
        if s[j] in res:
            res = res.split(s[j])[-1]
        res += s[j]
        j += 1
        n = max(n, len(res))
    return n


print(lengthOfLongestSubstring("pwwkew"))


"""
上述算法运用了"滑窗算法"，每遍历一个字符判断是否出现在窗口中，若没有，则加入，若有，则把窗口中此字符之前的字符串丢弃并加入当前字符。
存储最大的子串的长度。
"""

"""
若是求最大子串？？？
"""


def LongestSubstring(s):
    """
    求字符串的最大子串
    :param s:
    :return:
    """
    res = ''
    sub = ''
    j = 0
    while j < len(s):
        if s[j] in res:
            res = res.split(s[j])[-1]
        res += s[j]
        j += 1
        if len(res) > len(sub):
            sub = res
    return sub


print(LongestSubstring("abcabcdbb"))
