# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ([-inf, root, inf])
        # minimum , node, maximum
        # if node not within range, return false, else continue
        #if node.left: add q.append(minimum, node.left, node.val)
        #if node.right: q.append(node.val, node.right, maximum)
        q = deque([((float("-inf")), root, float("inf"))])
        while q:
            minimum, node, maximum = q.popleft()
            if not (minimum < node.val < maximum):
                return False
            if node.left:
                q.append((minimum, node.left, node.val))
            if node.right:
                q.append((node.val, node.right, maximum))
        return True