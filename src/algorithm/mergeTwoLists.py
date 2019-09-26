class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    res = ListNode(0)
    cur = res
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 is not None:
        cur.next = l1
    if l2 is not None:
        cur.next = l2
    return res.next


l1 = ListNode(5)
l2 = ListNode(0)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l3 = mergeTwoLists(l1, l2)
print(l3)
