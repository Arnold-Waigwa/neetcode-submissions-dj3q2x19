# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #we can have two values [node, greatest]
        # [2, -inf]
        #if 2 >= inf: good += 1 else 0
        #if node.left
        # q.append([node.left, max(node.val, greatest)])
        q = deque([(root, float("-inf"))])
        good = 0
        while q:
            node, greatest = q.popleft()
            good += 1 if node.val >= greatest else 0
            if node.left:
                q.append((node.left, max(node.val, greatest)))
            if node.right:
                q.append((node.right, max(node.val, greatest)))
        return good

        