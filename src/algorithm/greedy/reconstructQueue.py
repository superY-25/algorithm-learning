"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
"""

class Solution:
    def reconstructQueue(self, people: list) -> list:
        """
        思路：插入排序，失败
        :param people:
        :return:
        """
        size = len(people)
        if size == 0 or size == 1:
            return people
        ret = [people[0]]
        for i in range(1, size):
            item = people[i]
            for j in range(len(ret)):
                temp = ret[j]
                if item[1] == temp[1]:
                    if item[0] > temp[0]:
                        ret.insert(j, item)
                        break
                    else:
                        continue
                elif item[1] < temp[1]:
                    ret.insert(j, item)
                    break
            ret.append(item)
        return ret

    def reconstructQueue1(self, people: list) -> list:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == '__main__':
    # s = Solution()
    # print(s.reconstructQueue1([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    # a.sort(key=lambda x: (-x[0], x[1]))
    # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    a.sort(key=lambda x: -x[0])
    print(a)
