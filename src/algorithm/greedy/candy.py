
"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
"""

class Solution:
    def candy(self, ratings: list) -> int:
        cur = 0
        ret = 0
        ratings_n = len(ratings)
        i = 0
        while i < ratings_n:
            if i == 0:
                if ratings[i] > ratings[i + 1]:
                    cur = 2
                    ret += 2
                else:
                    cur = 1
                    ret += 1
            elif 0 < i < ratings_n - 1:
                if ratings[i] > ratings[i + 1]:
                    temp_s = 0
                    cur = 1
                    while i < (ratings_n - 1) and ratings[i] > ratings[i + 1]:
                        temp_s += cur
                        cur += 1
                        i += 1
                    temp_s += cur
                    ret += temp_s
                    cur = 1
                else:
                    ret += cur
            else:
                if ratings[i] > ratings[i - 1]:
                    ret = ret + cur + 1
                else:
                    ret += 1
            i += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.candy([3,2,2,1,0,2]))

