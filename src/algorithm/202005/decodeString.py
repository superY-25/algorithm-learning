

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (str, int) 记录之前的字符串和括号外的上一个数字
        num = 0
        res = ""  # 实时记录当前可以提取出来的字符串
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.decodeString('a3[q2[c]]'))

