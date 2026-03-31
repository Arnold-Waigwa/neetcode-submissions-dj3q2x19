# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # "1,2,N,N,3,4,N,N,5,N,N"
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def preorder(node):
            if not node:
                data.append("N")
            else:
                data.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ",".join(data)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if data[i] == "N":
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        
        
