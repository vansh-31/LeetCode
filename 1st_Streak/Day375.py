# Problem : Amount of Time for Binary Tree to Be Infected
# Problem Statement : You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        parent = {}
        def pre(root, parentNode):
            if not root:
                return
            nonlocal start
            if start == root.val:
                start = root
            parent[root] = parentNode
            pre(root.left, root)
            pre(root.right, root)
        pre(root, None)
        ans = 0
        vis = set()
        def infect(root, time):
            if not root:
                return
            nonlocal ans
            ans = max(ans, time)
            vis.add(root)
            if root.left not in vis:
                infect(root.left, time + 1)
            if root.right not in vis:
                infect(root.right, time + 1)
            if parent[root] not in vis:
                infect(parent[root], time + 1)

        infect(start, 0)
        return ans
