# Problem : Delete Leaves With a Given Value
# Problem Statement : Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def solve(root):
            if not root:
                return None
            root.left = solve(root.left)
            root.right = solve(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            return root

        return solve(root)
