
"""
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walking-robot-simulation
"""
class Solution:
    def robotSim(self, commands: list, obstacles: list) -> int:
        """
        时间复杂度 O(M * N) M为commands的长度  N为obstacles的长度
        :param commands:
        :param obstacles:
        :return:
        """
        position = [0, 0]
        direction = 'N'
        size = len(commands)
        ret = 0
        for i in range(size):
            if commands[i] == -2:  # 向左转
                if direction == 'N':
                    direction = 'W'
                elif direction == 'E':
                    direction = 'N'
                elif direction == 'S':
                    direction = 'E'
                elif direction == 'W':
                    direction = 'S'
                continue
            elif commands[i] == -1:  # 向右转
                if direction == 'N':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'N'
                continue
            else:
                if direction == 'N':
                    new = position[1] + commands[i]
                    for item in obstacles:
                        if item[0] == position[0] and position[1] < item[1] <= new:
                            new = item[1] - 1
                    position[1] = new
                elif direction == 'E':
                    new = position[0] + commands[i]
                    for item in obstacles:
                        if item[1] == position[1] and position[0] < item[0] <= new:
                            new = item[0] - 1
                    position[0] = new
                elif direction == 'S':
                    new = position[1] - commands[i]
                    for item in obstacles:
                        if item[0] == position[0] and new <= item[1] < position[1]:
                            new = item[1] + 1
                    position[1] = new
                elif direction == 'W':
                    new = position[0] - commands[i]
                    for item in obstacles:
                        if item[1] == position[1] and new <= item[0] < position[0]:
                            new = item[0] + 1
                    position[0] = new
            ret = max(ret, position[0] ** 2 + position[1] ** 2)
        return ret

    def robotSim1(self, commands, obstacles):
        dx = [0, 1, 0, -1]  # 表示x方向上的增加还是减少
        dy = [1, 0, -1, 0]  # 表示y方向上的增加还是减少
        x = y = di = 0  # x y的初始值和
        obstacleSet = set(map(tuple, obstacles))  # 这里需要这样转换，否则时间超时
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)
                    else:
                        break

        return ans


if __name__ == '__main__':
    # s = Solution()
    # print(s.robotSim1([-2,8,3,7,-1], [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]))
    a = [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]
    # print([1,4] in a)
    obstacleSet = set(map(tuple, a))
    print(obstacleSet)