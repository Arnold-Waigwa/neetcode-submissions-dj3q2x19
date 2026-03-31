class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            # Both nodes are None, so they are the same
            if not node1 and not node2:
                return True
            # One of the nodes is None, or values don't match, so they aren't the same
            if not node1 or not node2 or node1.val != node2.val:
                return False
            # Recursively check left and right subtrees
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
        
        # Base case: if subRoot is None, it's trivially a subtree
        if not subRoot:
            return True
        # If root is None and subRoot is not, subRoot can't be a subtree
        if not root:
            return False
        # Check if the trees are the same starting from the current node in root
        if isSameTree(root, subRoot):
            return True
        # Otherwise, check recursively in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
