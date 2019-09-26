"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

link：https://leetcode-cn.com/problems/add-two-numbers
"""


class LinkNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    pre = 0
    first = LinkNode(0)
    curr = first
    while l1 is not None or l2 is not None:
        if l1 is None:
            x = 0
        else:
            x = l1.val
            l1 = l1.next
        if l2 is None:
            y = 0
        else:
            y = l2.val
            l2 = l2.next
        s = x + y + pre
        pre = s // 10
        curr.next = LinkNode(s % 10)
        curr = curr.next
    if pre == 1:
        curr.next = LinkNode(pre)
    return first.next



"""
列表类型
"""

def addTwoNumbers1(l1, l2):
    pre = 0
    l3 = []
    i, j = 0, 0
    while i < len(l1) or j < len(l2):
        if l1[i] is None:
            x = 0
        else:
            x = l1[i]
        if l2[j]is None:
            y = 0
        else:
            y = l2[j]
        s = x + y + pre
        m = s % 10
        pre = s // 10
        l3.append(m)
        i += 1
        j += 1
    if pre == 1:
        l3.append(pre)
    return l3


print(addTwoNumbers1([2, 4, 3], [5, 6, 4]))
