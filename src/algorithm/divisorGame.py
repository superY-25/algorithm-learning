"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
"""


def divisorGame(N):
    """
    基本思路：
        将所有的小于等于 N 的解都找出来，基于前面的，递推后面的。
        状态转移: 如果 i 的约数里面有存在为 False 的（即输掉的情况），则当前 i 应为 True；如果没有，则为 False
    :param N:
    :return:
    """
    target = [0 for i in range(N + 1)]
    target[1] = 0  # 若爱丽丝抽到1，则爱丽丝输
    if N <= 1:
        return False
    else:

        target[2] = 1  # 若爱丽丝抽到2，则爱丽丝赢
        for i in range(3, N + 1):
            for j in range(1, i // 2):
                # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                if i % j == 0 and target[i - j] == 0:
                    target[i] = 1
                    break
        return target[N] == 1


def divisorGame1(N):
    """
    基本思路：
        最终结果应该是占到 2 的赢，占到 1 的输；
        若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；
        若当前为偶数， 偶数的约数可以是奇数可以是偶数也可以是 1，因此直接减 1，则下一个是奇数；
        因此，奇则输，偶则赢。
    :param N:
    :return:
    """
    return N % 2 == 0
