

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            level_size = len(q)  # Track the number of nodes at this level
            for i in range(level_size):
                node = q.popleft()
                
                # Only append the last node of the level to the result
                if i == level_size - 1:
                    res.append(node.val)
                
                # Add children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
