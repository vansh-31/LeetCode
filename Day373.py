# Problem : Range Sum of BST
# Problem Statement : Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0

        def solve(root):
            nonlocal ans
            if not root:
                return
            if low <= root.val <= high:
                ans += root.val
            solve(root.left)
            solve(root.right)

        solve(root)
        return ans
