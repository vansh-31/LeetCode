# Problem : Sum Root to Leaf Numbers
# Problem Statement : You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        v = []
        num = ""

        def solve(root, num):
            if root == None:
                return
            num += str(root.val)
            if root.left == None and root.right == None:
                v.append(int(num))
                return
            solve(root.left, num)
            solve(root.right, num)

        solve(root, num)
        return sum(v)
