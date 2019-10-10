"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head: ListNode):
    """
    此算法可以不用限制链表是否已排好序，空间复杂度O(n),时间复杂度O(n)
    :param head:
    :return:
    """
    if head is None:
        return head
    vals = [head.val]
    pre = head
    curr = head.next
    while curr is not None:
        if curr.val not in vals:
            vals.append(curr.val)
            pre = curr
            curr = curr.next
        else:
            curr = curr.next
            pre.next = curr
    return head


def deleteDuplicates1(head: ListNode):
    if head is None:
        return head
    pre = head
    curr = head.next
    while curr is not None:
        if curr.val != pre.val:
            pre = curr
            curr = curr.next
        else:
            curr = curr.next
            pre.next = curr
    return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
h = deleteDuplicates1(l)
print(h.val)
