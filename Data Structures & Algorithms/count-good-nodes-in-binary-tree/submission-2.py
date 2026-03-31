# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #perform a dfs(node, biggestsofar)
        #in every iteration, if its >= biggest so far, give it 1 else 0
        # update biggest so far for next node
        # return isgoodnode + leftgoodNode + rightgoodNode
        def dfs(node, biggest_so_far):
            if not node: return 0
            isGood = 1 if node.val >= biggest_so_far else 0

            biggest_so_far = max(node.val, biggest_so_far)

            leftGood = dfs(node.left, biggest_so_far)
            rightGood = dfs(node.right, biggest_so_far)

            return isGood + leftGood + rightGood
        return dfs(root, root.val)
        