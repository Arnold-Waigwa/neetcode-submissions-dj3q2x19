# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #every child returns the maximum of their left or right
        #start from the root
        #every node gets to update nonlocal for potential max
        maximum = float("-inf")
        def dfs(node):
            nonlocal maximum
            if not node: return 0
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))
            maximum = max(maximum, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return maximum
