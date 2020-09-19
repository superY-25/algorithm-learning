"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
"""


class Solution:
    def majorityElement(self, nums: list) -> int:
        """
        内存消耗太大
        :param nums:
        :return:
        """
        dic = {}
        for e in nums:
            if dic.get(e) is None:
                dic[e] = 1
            else:
                dic[e] = dic[e] + 1
        cur_k, cur_v = 0, 0
        for key, value in dic.items():
            if cur_v < value:
                cur_k = key
                cur_v = value
        return cur_k


if __name__ == '__main__':
    nums = [3,2,3]
    s = Solution()
    print(s.majorityElement(nums))
