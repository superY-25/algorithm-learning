"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = pre_head = ListNode(0)
        pos = pos_head = ListNode(0)
        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                pos.next = head
                pos = pos.next
            head = head.next
        pos.next = None
        pre.next = pos_head.next
        return pre_head.next


if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(1)
    s = Solution()
    print(s.partition(head, 2))
