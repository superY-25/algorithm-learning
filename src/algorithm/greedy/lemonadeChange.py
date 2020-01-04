




class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        """
        贪心算法 每次需要找零时，都用能找到的最大金额找零。比如 有零钱 5 5 5 10 需要找零15 则用 10和5的组合找零。
        :param bills:
        :return:
        """
        temp = []
        n_bills = len(bills)
        try:
            for i in range(n_bills):
                if bills[i] == 5:
                    temp.append(5)
                if bills[i] == 10:
                    # 找零
                    if 5 in temp:
                        temp.remove(5)
                        temp.append(10)
                    else:
                        return False
                if bills[i] == 20:
                    # 找零
                    if 10 in temp and 5 in temp:
                        temp.remove(10)
                        temp.remove(5)
                    else:
                        temp.remove(5)
                        temp.remove(5)
                        temp.remove(5)
            return True
        except:
            return False

    def lemonadeChange1(self, bills: list) -> bool:
        """
        贪心算法 每次需要找零时，都用能找到的最大金额找零。比如 有零钱 5 5 5 10 需要找零15 则用 10和5的组合找零。
        上面算法的改进 将temp数组替换成5 和 10 的标识
        :param bills:
        :return:
        """
        f, t = 0, 0
        n_bills = len(bills)
        for i in range(n_bills):
            if bills[i] == 5:
                f += 1
            if bills[i] == 10:
                # 找零
                if f > 0:
                    f -= 1
                    t += 1
                else:
                    return False
            if bills[i] == 20:
                # 找零
                if t > 0 and f > 0:
                    t -= 1
                    f -= 1
                elif f > 3:
                    f = f - 3
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange1([10,10]))
