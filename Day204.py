# Problem : All Possible Full Binary Trees
# Problem Statement : Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0 or n < 1: return []
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, n + 1):
            for j in range(1, i):
                left_subtrees = dp[j]
                right_subtrees = dp[i - 1 - j]

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(0)
                        root.left = left_subtree
                        root.right = right_subtree
                        dp[i].append(root)
        return dp[n]