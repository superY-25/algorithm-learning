"""
求字符串最后一个单词的长度
"""

def lengthOfLastWord(s):
    s = s.rstrip(' ')
    if ' ' not in s:
        return len(s)
    res = 0
    for i in reversed(s):
        if i == ' ':
            break
        res = res + 1
    return res


print(lengthOfLastWord('Hello World   '))
