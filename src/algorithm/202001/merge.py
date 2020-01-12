"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
"""


class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x: x[0])
        ret = []
        for item in intervals:
            if not ret or ret[-1][1] < item[0]:
                ret.append(item)
            else:
                ret[-1][1] = max(ret[-1][1], item[1])
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[15,18],[2,6],[8,10]]))