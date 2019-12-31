"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
"""


class Solution:

    def getPermutation1(self, n: int, k: int) -> str:
        """
        分析：
        :param n:
        :param k:
        :return:
        """
        lst = [i for i in range(1, n+1)]
        ret = ''
        while k >= 0 and n > 0:
            t = self.factorial(n - 1)
            m = k % t
            v = k // t
            if k == 0:
                ret += str(lst[n - 1])
                lst.pop(n - 1)
            elif m > 0:
                ret += str(lst[v])
                lst.pop(v)
            else:
                ret += str(lst[v - 1])
                lst.pop(v - 1)
            k = m
            n = n - 1
        return ret

    def factorial(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation1(3, 6))
    # s = 456
    # print(list(str(s)))
