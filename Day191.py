# Problem : Minimum Depth of Binary Tree
# Problem Statement : Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if root.left and root.right:
            return min(left, right) + 1
        
        return max(left, right) + 1