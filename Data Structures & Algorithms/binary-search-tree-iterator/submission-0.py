# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = 0
        self.iterator = [float("-inf")]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.iterator.append(root.val)
            dfs(root.right)
        dfs(root)
    def next(self) -> int:
        if self.hasNext():
            self.pointer += 1
            return self.iterator[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.iterator) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()