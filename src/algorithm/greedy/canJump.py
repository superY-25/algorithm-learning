"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
"""


class Solution:
    def canJump(self, nums: list) -> bool:
        """
        超时
        :param nums:
        :return:
        """
        size = len(nums)
        if not nums:
            return False
        if size == 1:
            return True
        q = [{0: nums[0]}]
        while q:
            temp = q.pop(0)
            for index, value in temp.items():
                for i in range(1, value + 1):
                    if index + i == size - 1 and nums[index + i] == nums[-1]:
                        return True
                    elif index + i < size and nums[index + i] != 0:
                        q.append({index + i: nums[index + i]})
        return False


    def canJump1(self, nums):
        """
        贪心算法
        :param nums:
        :return:
        """
        max_i = 0  # 初始化当前能到达最远的位置
        size = len(nums)
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
            if max_i == size - 1:
                return True
        return max_i >= i


if __name__ == '__main__':
    s = Solution()
    print(s.canJump1([1,2,0,1,0]))
