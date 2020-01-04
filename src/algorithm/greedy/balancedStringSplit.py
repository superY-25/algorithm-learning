"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        ret = 0
        for i in s:
            if i == 'R':
                r += 1
            if i == 'L':
                l += 1
            if r == l:
                ret += 1
                r, l = 0, 0
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.balancedStringSplit('RLRRLLRLRL'))
