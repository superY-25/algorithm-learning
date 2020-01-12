"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        有多少行设置多少个数组，按顺序放入排列的数组中。
        :param s:
        :param numRows:
        :return:
        """
        if numRows == 1:
            return s
        ret = ['' for _ in range(numRows)]
        flag = 1
        i = 0
        for c in s:
            ret[i] = ret[i] + c
            if i == (numRows - 1):
                flag = -1
            elif i == 0:
                flag = 1
            i += flag
        return ''.join(ret)



if __name__ == '__main__':
    s = Solution()
    print(s.convert("ABC", 1))
