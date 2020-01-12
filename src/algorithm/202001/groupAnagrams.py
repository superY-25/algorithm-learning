"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
"""

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        """
        通过hash映射。
        :param strs:
        :return:
        """
        dic = {}
        for item in strs:
            s = ''.join(sorted(item))
            temp = dic.get(s)
            if temp is None:
                dic.setdefault(s, [item])
            else:
                dic[s].append(item)
        return list(dic.values())





if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # a = {}
    # print(a.get('u'))