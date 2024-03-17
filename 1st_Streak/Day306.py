# Problem : Count Nodes Equal to Average of Subtree
# Problem Statement : Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
# Note:
# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def solve(root):
            if not root:
                return (0, 0)
            left = solve(root.left)
            right = solve(root.right)
            subtree_sum = root.val + left[0] + right[0]
            subtree_nodes = 1 + left[1] + right[1]
            subtree_avg = subtree_sum // subtree_nodes
            if subtree_avg == root.val:
                nonlocal count
                count += 1
            return (subtree_sum, subtree_nodes)

        solve(root)
        return count
