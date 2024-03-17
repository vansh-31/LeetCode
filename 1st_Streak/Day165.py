# Problem : Minimum Absolute Difference in BST
# Problem Statement : Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        In = []
        def Inorder(root):
            if root:
                Inorder(root.left)
                In.append(root.val)
                Inorder(root.right)
        Inorder(root)
        ans = math.inf
        for i in range(len(In)-1):
            ans = min(ans, In[i+1]-In[i])
        return ans