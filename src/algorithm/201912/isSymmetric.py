
"""
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.right is None and root.left is None):
            return True
        q = [root]
        k = 2
        lst = []
        m = 0
        while q:
            n = q.pop(0)
            if n.left is not None:
                lst.append(n.left.val)
                q.append(n.left)
                m += 1
            else:
                lst.append('n')
            if n.right is not None:
                lst.append(n.right.val)
                q.append(n.right)
                m += 1
            else:
                lst.append('n')
            if len(lst) == k:
                if lst == lst[::-1]:
                    k = 2 * m
                    m = 0
                    lst = []
                else:
                    return False
        return True


if __name__ == '__main__':
    [4, 63, 63, 3, 64, 3, 64, 39, -45, -57, 84, -45, 39, -57, 84]
    root = TreeNode(3)
    root.left = TreeNode(63)
    root.right = TreeNode(63)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(64)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(64)
    s = Solution()
    print(s.isSymmetric(root))
