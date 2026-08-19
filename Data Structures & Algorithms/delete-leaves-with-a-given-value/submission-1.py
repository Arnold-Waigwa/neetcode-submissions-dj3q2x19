# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node.left and not node.right:
                if node.val == target:
                    return True
                return False

            left = right = None
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            if left:
                node.left = None
            if right:
                node.right = None
            
            if not node.left and not node.right and node.val == target:
                return True
            return False
        
        if dfs(root):
            return None
        return root
            
