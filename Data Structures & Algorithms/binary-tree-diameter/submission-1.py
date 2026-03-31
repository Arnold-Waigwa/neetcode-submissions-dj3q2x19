# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node: return 0
            right = dfs(node.right)
            left = dfs(node.left)

            diameter = max(diameter, right + left)

            return 1 + max(right, left)
        dfs(root)
        return diameter