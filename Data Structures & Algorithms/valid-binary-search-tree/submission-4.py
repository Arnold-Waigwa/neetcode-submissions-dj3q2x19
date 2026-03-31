# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #(valid)?
        # node.left < node < key
        #valid?
        #a node returns true if only the previous nodes are true
        #and if it satisfies the inequality node.left < node < key
        minimum, maximum = float("-inf"), float("inf")
        if not root: return True
        def dfs(minimum, node, maximum):
            if not node: return True
            if minimum >= node.val or node.val >= maximum:
                return False
            else:
                return dfs(minimum, node.left, node.val) and dfs(node.val, node.right, maximum)
        return dfs(minimum, root, maximum)
       
