# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize a q with the root and a result list
        # While that queue exists:
        #create an array.
        #for every i in range of length of q at that point:
        #popleft and add its children to the q. and add the node into
        # the array. At the end of the loop, append it to the res list
        if not root: return []
        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


        