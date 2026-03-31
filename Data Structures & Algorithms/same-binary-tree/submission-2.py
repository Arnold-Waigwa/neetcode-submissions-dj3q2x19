# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p: return True

        q = deque([q])
        p = deque([p])

        while q and p:
            nodeq = q.popleft()
            nodep = p.popleft()

            if nodeq is None and nodep is None:
                continue
            if nodeq is None or nodep is None or nodeq.val != nodep.val:
                return False

            q.append(nodeq.left)
            q.append(nodeq.right)
            p.append(nodep.left)
            p.append(nodep.right)

        return True