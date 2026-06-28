# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #deque root,root.val :  q = deque([(root.val,root)])
        #good_nodes = 0
        #while q exists: for i in the len(q) at this point,
        #child = i[0], parent = i[1]
        #if child >= parent: add count + 1,
        #q.append(node.left, max(child, parent))
        #q.append(node.right, max(child, parent))
        if not root: return 0
        q = deque([(root, root.val)])
        good_nodes = 0
        while q:
            child, parent = q.popleft()
            if child.val >= parent: good_nodes += 1
            if child.left:
                q.append((child.left, max(child.val, parent)))
            if child.right:
                q.append((child.right, max(child.val, parent)))
        return good_nodes