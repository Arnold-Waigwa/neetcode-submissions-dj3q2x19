# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #-inf < 2.val < inf
        #min < root.left < 2.val
        #at any occasion
        def dfs(minimum, node, maximum):
            if not node: return True
            #are you not within your range?
            if not (minimum < node.val < maximum):
                return False
            return dfs(minimum, node.left, node.val) and dfs(node.val, node.right, maximum)
        return dfs(float("-inf"), root, float("inf"))
