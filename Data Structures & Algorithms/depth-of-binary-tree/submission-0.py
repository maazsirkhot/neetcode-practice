# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maximumDepth = 0

        def dfs(node, currentHeight):
            if not node:
                self.maximumDepth = max(self.maximumDepth, currentHeight)
                return currentHeight

            dfs(node.left, currentHeight + 1)
            dfs(node.right, currentHeight + 1)

        dfs(root, 0)
        return self.maximumDepth