# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        a target will either be bigger or smaller than a curr node
        therefore, we can only install at a root since the target isn't
        already there
        algorithm:
        compare the curr node with the target. if its bigger, recurse 
        right, if its smaller recurse left. if we reach a null node
        if its smaller and no left child, place it as the left,
        if its smaller and no right child, place it as right
        """
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        return root
            