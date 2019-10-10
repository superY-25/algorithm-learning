# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        """
        使用递归的方式来遍历
        :param root:
        :return:
        """
        if root == None:
            return None
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res):
        if root.left != None:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right != None:
            self.helper(root.right, res)

    def inorderTraversal1(self, root: TreeNode):
        """
        使用非递归的方式来中序遍历二叉树
        :param root:
        :return:
        """
        stack = ['?']
        res = []
        if root != None:
            while (root is not None and root != '?') or len(stack) > 0:
                while root != None:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if root != '?':
                    res.append(root.val)
                    root = root.right
        return res



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.inorderTraversal1(root))
