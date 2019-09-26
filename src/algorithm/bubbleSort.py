
"""
冒泡排序算法思想：遍历数组大的元素往后调换位置
算法的时间复杂度：最坏是O(n^2),最好是O(n),平均O(n^2) 
"""


def bubbleSort(num):
    size = len(num) - 1
    for i in range(size):
        flag = 0
        for j in range(size - i):
            if num[j] > num[j + 1]:
                temp = num[j]
                num[j] = num[j + 1]
                num[j + 1] = temp
                flag = 1
        if flag is 0:
            break
    return num


print(bubbleSort([5, 13, 14, 3, 9, 0, 6, 4, 1, 2, 7, 11, 8, 12]))
