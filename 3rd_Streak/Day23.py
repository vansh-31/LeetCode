# Problem : Smallest String Starting From Leaf
# Problem Statement : You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller.
# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = chr(ord("a") + 26)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], cur_str: str):
            if not node:
                return
            cur_str = chr(ord("a") + node.val) + cur_str
            if not node.left and not node.right:
                if cur_str < self.res:
                    self.res = cur_str
            else:
                if node.left:
                    dfs(node.left, cur_str)
                if node.right:
                    dfs(node.right, cur_str)

        dfs(root, "")
        return self.res
