# Problem : Construct String from Binary Tree
# Problem Statement : Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(root):
            if not root:
                return ""
            curr = str(root.val)
            left = solve(root.left)
            right = solve(root.right)
            if right:
                return f"{curr}({left})({right})"
            if left:
                return f"{curr}({left})"
            return curr

        return solve(root)
