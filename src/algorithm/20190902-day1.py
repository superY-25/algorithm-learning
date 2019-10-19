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


def lastNoK(nums, k):
    """
    输出单链表中的倒数第k个元素值, 这里假设python list是一个单链表
    :param nums:
    :param k:
    :return:
    """
    nums_len = len(nums)
    if k > nums_len:
        return None
    pre, cur, i = 0, 0, 0
    for n in nums:
        cur += 1
        if i >= k:
            pre += 1
        i += 1
    return nums[pre]


print(lastNoK([1, 2, 3, 4, 5, 6, 7, 8], 3))


"""
总结：第一题类似排序，将奇数排到偶数前面，遍历数组，遇到奇数，若前面有偶数就将其往前移动，所以这里涉及到元素的移动。时间复杂度O(n^2)
     第二题的思路就是使用双指针，遍历单链表时两个指针的间距就是k，遍历完成是后一个指针的位置就是倒数第k个元素的位置。
"""