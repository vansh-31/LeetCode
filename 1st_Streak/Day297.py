# Problem : Find Largest Value in Each Tree Row
# Problem Statement : Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append((root, 0))
        while q:
            node, lvl = q.popleft()
            if lvl == len(ans):
                ans.append(node.val)
            ans[lvl] = max(ans[lvl], node.val)
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))
        return ans
