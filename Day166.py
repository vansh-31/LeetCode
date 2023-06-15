# Problem : Maximum Level Sum of a Binary
# Problem Statement : Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = []
        q.append((root,1))
        levelSums = defaultdict(int)
        while q:
            node,lvl = q.pop(0)
            levelSums[lvl] += node.val
            if node.left:
                q.append((node.left,lvl+1))
            if node.right:
                q.append((node.right,lvl+1))
        print(levelSums)
        mx,lvl = root.val,1
        for key,value in levelSums.items():
            if value > mx:
                mx = value
                lvl = key
        return lvl