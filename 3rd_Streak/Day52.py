# Problem :
# Problem Statement :
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        def solve(root):
            if root.val <= 1:
                return root.val == 1
            left = solve(root.left)
            right = solve(root.right)
            if root.val == 2:
                return left or right
            else:
                return left and right

        return solve(root)
