# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        res = []
        if there's not root return []
        dfs(node, level)
        base case return None
        if len(res) == level: first element of the level
            create new array, and append the element, and append it
            to the res
        otherwise:
            append the child to res[level]
        
        dfs(left, +1)
        dfs(right, +1)
        """
        if not root:
            return []

        res = []
        def dfs(node, level):
            if not node:
                return 
            
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res











