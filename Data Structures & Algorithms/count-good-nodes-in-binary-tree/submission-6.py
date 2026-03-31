# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #bfs
        """
        already know we need a second variable greatest
        just use [], () some two parameter storage
        add one if greatest >= node[node, greatest] 
        then add children
        """
        if not root: return 0
        good = 0
        q = deque([(root, root.val)])
        while q:
            node, greatest = q.popleft()
            good += 1 if node.val >= greatest else 0
            greatest = max(node.val, greatest)
            if node.left: q.append((node.left, greatest))
            if node.right: q.append((node.right, greatest))
        return good