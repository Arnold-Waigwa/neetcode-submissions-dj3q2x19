# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def preorder(node):
            if not node: 
                data.append("N")
                return
            data.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0
        def preorder():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()
            

            


