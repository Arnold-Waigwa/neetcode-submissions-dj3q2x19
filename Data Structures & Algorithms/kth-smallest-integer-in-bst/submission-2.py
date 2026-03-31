# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we know a bst inorder search gets values in order
        #Perform a dfs(inorder) and return the smallest
        res = 0
        def inorder(node):
            nonlocal res, k
            if not node:
                return None
            inorder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inorder(node.right)
        inorder(root)
        return res

