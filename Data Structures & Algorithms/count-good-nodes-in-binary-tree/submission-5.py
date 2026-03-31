# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        initialize good = 0
        Start at the root, create a custom dfs with two
        parameters. if not node, return None
        compare the node to the 2cond parameter greatest
        if node.val > greatest; good += 1
        greatest = max(greatest, node.val)
        dfs(node.left) 
        dfs(node.right)
        """
        good = 0
        def dfs(node, greatest):
            nonlocal good
            if not node: return None
            good += 1 if node.val >= greatest else 0
            greatest = max(node.val, greatest)
            dfs(node.left, greatest)
            dfs(node.right, greatest)
        dfs(root, root.val)
        return good
        
        
        