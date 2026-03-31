# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        There is a relationship between two arrays and we have all info
        root will always be the first in the preorder array, set that to root
        then, get the index in the inorder array, call it mid
        left subtree = self.buildTree(preorder[1:mid + 1], inorder[:mid + 1])
        right subtree = self.buildTree(preorder[mid + 1:],inorder[m + 1:])
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        return root
