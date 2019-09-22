"""
两个算法：1、排序，将一个数组中的所有奇数放在偶数前面，保持原来的顺序不变。
        2、输出单链表中倒数第k节点。（思路(待实现)：定义两个指针，先将一个指针向前移动k个节点，然后两个节点同时向前移动，
           当第一个节点已经到达尾部时，第二个节点就是倒数第k个节点的位置，并将其输出即可）
"""


def oddonfrontofeven(arr):
    """
    思路：遍历整个数组，遇到奇数时，然后遍历前面的元素，遇到偶数则进行交换
    :param arr:
    :return:
    """
    print("before sort: ", arr)
    size = len(arr)
    for i in range(size):
        if arr[i] % 2 != 0:
            for j in range(i-1, -1, -1):
                if arr[j] % 2 == 0:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
    print("after sort: ", arr)


# oddonfrontofeven([2, 3, 4, 8, 7, 5, 11, 12, 14, 16, 19])


def oddonfrontofeven1(arr):
    """
    思路：此方法是上面方法的改进版本，在第二层循环中一旦循环到奇数时，则此数之前的所有数都是奇数，故不必在循环下去了，
         flag标识起到退出循环的作用
    :param arr:
    :return:
    """
    print("before sort: ", arr)
    size = len(arr)
    for i in range(size):
        if arr[i] % 2 != 0:
            flag = 0
            for j in range(i - 1, -1, -1):
                if (arr[j] % 2 == 0) and (flag == 0):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    flag = 0
                else:
                    flag = 1
                if flag == 1:
                    break
    print("after sort: ", arr)


oddonfrontofeven1([2, 3, 4, 8, 7, 5, 11, 12, 14, 16, 19])

