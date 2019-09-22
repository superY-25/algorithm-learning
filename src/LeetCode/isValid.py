"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串

link：https://leetcode-cn.com/problems/valid-parentheses
"""


def isValid(s: str) -> bool:
    """
    独立思考的答案，辅助空间 栈 O(n) 时间复杂度 O(n)
    :param s:
    :return:
    """
    temp = []
    left = '({['
    right = ')}]'
    if s == '':
        return True
    for elem in s:
        if elem in left:
            temp.append(elem)
        if elem in right:
            if len(temp) > 0 and ((elem == ')' and temp[-1] == '(') or (elem == '}' and temp[-1] == '{') or (elem == ']' and temp[-1] == '[')):
                temp.pop()
            else:
                temp.append(elem)
                break
    return len(temp) == 0


def isValid1(s: str) -> bool:
    """
    参数别人的代码 对上面方法的改进，算法思想一致，设计的部分数据结构不同导致代码简化很多
    执行时 性能也好很多
    :param s:
    :return:
    """
    dic = {'{': '}', '(': ')', '[': ']', '?': '?'}
    temp = ['?']
    for elem in s:
        if elem in dic.keys():
            temp.append(elem)
        else:
            if dic[temp.pop()] != elem:
                return False
    return len(temp) == 0


print(isValid("[]}"))

