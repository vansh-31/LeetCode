# Problem : Diameter of Binary Tree
# Problem Statement : Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return (0, 0)
            left = solve(root.left)
            right = solve(root.right)
            return (
                max(left[1] + right[1] + 1, left[0], right[0]),
                max(left[1], right[1]) + 1,
            )

        return solve(root)[0] - 1
