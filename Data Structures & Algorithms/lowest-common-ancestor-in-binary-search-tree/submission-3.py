# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #the trick here is the structure of a bst
        #if p and q are both bigger than node, dsf to the right
        #if they are smaller, dsf on the left
        #if the values are smaller and bigger , or one of the values equal
        #then that is the lca.
        if not root: return None
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
        

        