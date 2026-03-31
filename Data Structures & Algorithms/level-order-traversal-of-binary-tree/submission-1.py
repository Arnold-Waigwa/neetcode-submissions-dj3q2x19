# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we could use a bfs
        #initialize an array
        #use a while and for loop
        #deque the root and use a while loop. before the for loop
        #initialize another array
        #for i in the current length, pop the node:
        # add the children, and append the node.val to the array
        if not root: return []
        res = []
        q = deque()
        q.append(root)
        while q:
            array = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                array.append(node.val)
            res.append(array)
        return res
        