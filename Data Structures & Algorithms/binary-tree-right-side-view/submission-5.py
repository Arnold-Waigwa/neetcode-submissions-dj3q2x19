# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #want the right most side of a level
        #dfs wanna keep track of the level
        #go through the level array and extract the right most
        #key part is if the level == len(array): create subarray
        if not root: return []
        res = []
        def dfs(node, level):
            if not node: return None
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        result = []
        for array in res:
            result.append(array[-1])
        return result

        