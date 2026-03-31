# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, biggest_so_far):
            if not node:
                return 0
            is_good = 1 if node.val >= biggest_so_far else 0
            biggest_so_far = max(biggest_so_far, node.val)

            left_good = dfs(node.left, biggest_so_far)
            right_good = dfs(node.right, biggest_so_far)

            return is_good + left_good + right_good
        return dfs(root,root.val)
            
        