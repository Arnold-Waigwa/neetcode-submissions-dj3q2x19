# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #every node has its min and max and it has to be within range
        #for the left: min, node.left, node.val, for the right: node.val, node.right, max
        if not root: return True
        q = deque([(float("-inf"), root, float("inf"))])
        while q:
            minimum, node, maximum = q.popleft()
            if node and not (minimum < node.val < maximum):
                return False
            if node:
                q.append((minimum, node.left, node.val))
                q.append((node.val, node.right, maximum))
        return True



        