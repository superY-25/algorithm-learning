# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:


def rightSideView(r):
    if r is None:
        return None
    l = [r.val]
    left = r.left
    right = r.right
    while left is not None or right is not None:
        if right is not None:
            l.append(right.val)
        else:
            l.append(left)



r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(5)
r.right.right = TreeNode(4)
print(rightSideView(r))


