# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #key is to traverse level by level 
        #append the right most node of each level
        #initialize an array res and a queue q
        #while q is not empty
        #for i in current length, remove the node from the queue,
        #add it children, if i = len(q) - 1,(right most), append the node.value
        if not root: return []
        res, q = [], deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i == level_size - 1: res.append(node.val)
        return res
        