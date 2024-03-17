# Problem : Find Mode in Binary Search Tree
# Problem Statement : Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)
        mx = 0

        def solve(root):
            nonlocal mx
            if not root:
                return
            modes[root.val] += 1
            mx = max(mx, modes[root.val])
            solve(root.left)
            solve(root.right)

        solve(root)
        ans = []
        for key, val in modes.items():
            if val == mx:
                ans.append(key)
        return ans
