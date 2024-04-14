# Problem : Sum of Left Leaves
# Problem Statement : Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def solve(root, left):
            if root == None:
                return
            if root.left == None and root.right == None:
                nonlocal ans
                if left:
                    ans += root.val
                return
            solve(root.left, True)
            solve(root.right, False)

        solve(root, False)
        return ans
