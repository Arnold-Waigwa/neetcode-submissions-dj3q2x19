# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #start from the root, and take the max of the 
        # left and right subtree. Start with 1 + depth
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        