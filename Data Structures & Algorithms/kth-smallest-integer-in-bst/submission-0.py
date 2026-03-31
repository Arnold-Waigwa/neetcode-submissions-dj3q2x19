# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        think of an inorder traversal of a bst
        will always be in order
        k = 4-1,3-1,2-1,1-1,0
        2,3,4,5
        if not root:
            return None
            visit(left)
            visit(parent)
            visit(right)
        """
        if not root: return None
        array = []
        def dfs(node):
            if not node: return None
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        dfs(root)
        return array[k-1]


        