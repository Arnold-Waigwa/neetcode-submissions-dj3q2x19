# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        count = 0
        while q:
            node, greatest = q.popleft()
            if node.val >= greatest:
                count += 1
                greatest = node.val
            if node.left:
                q.append((node.left, greatest))
            if node.right:
                q.append((node.right, greatest))
        return count


        