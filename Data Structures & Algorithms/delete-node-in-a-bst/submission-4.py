# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        three cases if we find a node to delete:
        1. it's a leaf -> simly return None
        2. it has one child -> return the child
        3. it has two childer:
                - find the smallest value of the right branch
                (we can guarantee that it will be a leaf)
                - replace that reference with the node to be del
                - return none
        """
        if not root:
            return 
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root



                
            

        
            