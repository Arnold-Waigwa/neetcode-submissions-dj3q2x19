# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pque,qque = deque([p]), deque([q])
        while pque and qque:

            qlen, plen = len(qque), len(pque)
            for _ in range(plen):
                nodep, nodeq = pque.popleft(), qque.popleft()
                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodeq.val != nodep.val:
                    return False

                pque.append(nodep.left)
                pque.append(nodep.right)
                qque.append(nodeq.left)
                qque.append(nodeq.right)

        return True

    


        