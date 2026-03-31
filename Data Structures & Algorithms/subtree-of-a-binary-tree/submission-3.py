# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False
            return isSame(nodep.left, nodeq.left) and isSame(nodep.right, nodeq.right)

        if not subRoot:
            return True

        if not root:
            return False
        
        if not isSame(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return True

        