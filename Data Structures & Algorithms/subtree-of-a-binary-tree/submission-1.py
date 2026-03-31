# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(nodep, nodeq):
            if not nodep and not nodeq: return True

            #if one is a node or the vals dont match return false

            if not nodep or not nodeq or nodep.val != nodeq.val: return False

            #else continue recursion

            return isSameTree(nodep.left, nodeq.left) and isSameTree(nodep.right, nodeq.right)

        #we wanna check from every node if its a subtree
        if not root: return False
        if not subRoot: return False

        #check if each node is a subtree by checking if its sametree starting at root
        if isSameTree(root, subRoot):
            return True

        #if not, recurse it
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        #helper function isSameTree
        
        


        