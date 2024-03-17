# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root:TreeNode) -> int:
        v = []
        num = ""
        def solve(root,num):
            if(root==None):
                return
            num += str(root.val)
            if root.left == None and root.right == None:
                v.append(int(num))
                return
            if (root.left):
                solve(root.left,num)
            if (root.right):
                solve(root.right,num)
        solve(root,num)
        return sum(v)