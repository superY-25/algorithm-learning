"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        """
        中序遍历 验证是否是升序排列
        :param root:
        :return:
        """
        if root is None:
            return True
        q = [root]
        pre = None
        while q:
            cur = q[len(1) - 1]
            if cur.left is not None:
                q.append(cur.left)
            if cur.left is None:
                q.remove(cur)
                if pre is not None and pre >= cur.val:
                    return False




    def isValidBST2(self, root: TreeNode) -> bool:
        """
        失败
        :param root:
        :return:
        """
        if root is None:
            return True
        q = [{'node': root, 'upper': None, 'lower': None}]
        while q:
            dic = q.pop(0)
            cur = dic['node']
            upper = dic['upper']
            lower = dic['lower']
            if cur.left is not None:
                if cur.left.val >= cur.val or (upper is not None and cur.left.val >= upper) or (lower is not None and cur.left.val <= lower):
                    return False
                q.append({'node': cur.left, 'upper': cur.val, 'lower': None})
            if cur.right is not None:
                q.append({'node': cur.right, 'upper': 'r', 'lower': cur.val})
                if cur.right.val <= cur.val or (upper is not None and lower == 'l' and cur.right.val >= lower):
                    return False
        return True

    def isValidBST1(self, root: TreeNode) -> bool:
        """
        递归 失败
        :param root:
        :return:
        """
        return self.judge(root, None, None)

    def judge(self, node: TreeNode, p, lower):
        pass


if __name__ == '__main__':
    a = [3, 1, 5, 0, 2, 4, 6]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    root.left.right.right = TreeNode(3)
    s = Solution()
    print(s.isValidBST(root))
