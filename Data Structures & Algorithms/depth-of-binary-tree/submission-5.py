# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #using a breadth first approach
        #deque the root, and while the queue is not empty
        #have a for loop that goes for i until len of queue
        #after for loop is done, add a one. After that, exit out
        res = 0
        if not root: return res
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res
            

        