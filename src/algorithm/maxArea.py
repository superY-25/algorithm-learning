"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

link：https://leetcode-cn.com/problems/container-with-most-water
"""


def maxArea(height):
    """
    双指针法，面积的大小取决于数值更小的那一边，
    :param height:
    :return:
    """
    max_area = 0
    l, r = 0, len(height) - 1
    while l < r:
        h = height[l] if height[l] < height[r] else height[r]
        max_area = max(max_area, h * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


print(maxArea([1, 8, 10, 2, 5, 4, 3, 10, 9]))


