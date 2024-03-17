# Problem : Unique Binary Search Trees II
# Problem Statement : Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(start, end):
            if start > end:
                return [
                    None,
                ]
            trees = []
            for root in range(start, end + 1):
                for left in solve(start, root - 1):
                    for right in solve(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees

        return solve(1, n)
