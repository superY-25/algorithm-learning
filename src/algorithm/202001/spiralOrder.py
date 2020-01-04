"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix: list) -> list:
        """
        遍历整个二维数组 时间复杂度O(m * n)
        算法改进 四条边可以一次性加入到lst列表中。根据上下左右判断是顺序还是逆序
        :param matrix:
        :return:
        """
        if not matrix:
            return matrix
        i, j = 0, 0
        row = len(matrix)
        column = len(matrix[0])
        n = row * column
        t, r, b, l = True, False, False, False
        t_, r_, b_, l_ = 0, 0, 0, 0
        lst = []
        while len(lst) < n:
            if t and len(lst) < n:
                lst.append(matrix[i][j])
                j += 1
                if j == column - t_:
                    i += 1
                    j -= 1
                    t = False
                    r = True
                    t_ += 1
            if r and len(lst) < n:
                lst.append(matrix[i][j])
                i += 1
                if i == row - r_:
                    j -= 1
                    i -= 1
                    r = False
                    b = True
                    r_ += 1
            if b and len(lst) < n:
                lst.append(matrix[i][j])
                j -= 1
                if j == -1 + b_:
                    j += 1
                    i -= 1
                    b = False
                    l = True
                    b_ += 1
            if l and len(lst) < n:
                lst.append(matrix[i][j])
                i -= 1
                if i == 0 + l_:
                    j += 1
                    i += 1
                    l = False
                    t = True
                    l_ += 1
        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9,10,11,12]
                        ]))
