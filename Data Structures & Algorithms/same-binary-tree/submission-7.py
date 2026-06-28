# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([q])
        p = deque([p])
        while p and q:
            qnode, pnode = q.popleft(), p.popleft()
            if not qnode and not pnode:
                continue
            if not qnode or not pnode or qnode.val != pnode.val:
                return False
            q.append(qnode.left)
            q.append(qnode.right)
            p.append(pnode.left)
            p.append(pnode.right)
        return not p and not q

        