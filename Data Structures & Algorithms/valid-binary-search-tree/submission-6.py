# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #lets do a bfs
        #key was making sure that the left side had an upper
        #bound of the parent node and the right side had a 
        #lower bound of the parent node.
        q = deque()
        mini, maxi = float("-inf"), float("inf")
        q.append((mini, root, maxi))
        while q:
            minimum, node, maximum = q.popleft()
            #check if the node is in the range
            if node.val <= minimum or node.val >= maximum:
                return False
            if node.left: 
                q.append((minimum, node.left, node.val))
            if node.right:
                q.append((node.val, node.right, maximum))
        return True

