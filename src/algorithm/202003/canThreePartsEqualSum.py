

class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        A_size = len(A)
        if A_size == 0:
            return False
        A_sum = sum(A)
        if A_sum % 3:
            return False
        target = A_sum // 3
        flag = 0
        temp = 0
        for e in A:
            temp += e
            if temp == target and flag < 2:
                flag += 1
                temp = 0
            elif flag == 2:
                flag = 3
        if flag == 2 and temp == target:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))