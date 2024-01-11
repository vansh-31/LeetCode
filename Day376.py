# Problem : Maximum Difference Between Node and Ancestor
# Problem Statement : Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root, mini, maxi, res):
            if not root:
                return
            res[0] = max(res[0], abs(mini - root.val), abs(maxi - root.val))
            mini = min(root.val, mini)
            maxi = max(root.val, maxi)
            dfs(root.left, mini, maxi, res)
            dfs(root.right, mini, maxi, res)

        res = [0]
        dfs(root, root.val, root.val, res)
        return res[0]
