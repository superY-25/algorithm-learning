# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    同时遍历两棵树（采用层次遍历法），判断其是否一致
    :param p:
    :param q:
    :return:
    """
    temp_p = []
    temp_q = []
    if p is not None:
        temp_p.append(p)
    if q is not None:
        temp_q.append(q)
    while len(temp_p) > 0 and len(temp_q) > 0:
        p = temp_p.pop(0)
        q = temp_q.pop(0)
        if p.val != q.val:
            return False
        if p.left is not None and q.left is not None:
            temp_p.append(p.left)
            temp_q.append(q.left)
        if (p.left is not None and q.left is None) or (p.left is None and q.left is not None):
            return False
        if p.right is not None and q.right is not None:
            temp_p.append(p.right)
            temp_q.append(q.right)
        if (p.right is not None and q.right is None) or (p.right is None and q.right is not None):
            return False
    if len(temp_p) != len(temp_q):
        return False
    return True


p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)

print(isSameTree(p, q))
