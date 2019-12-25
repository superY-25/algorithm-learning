"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
"""


def rorate(matrix: list):
    """
    先转置，然后再将每行翻转一下 时间复杂度O(N^2)
    :param matrix:
    :return:
    """
    row = len(matrix)
    # 转置
    for i in range(row):
        for j in range(i, row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 翻转每行
    for i in range(row):
        matrix[i] = matrix[i][::-1]
    return matrix


if __name__ == '__main__':
    m = [[1,2,3], [4,5,6], [7,8,9]]
    print(m)
    print(rorate(m))

