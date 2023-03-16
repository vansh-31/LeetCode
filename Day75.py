# Problem : Construct Binary Tree from Inorder and Postorder Traversal
# Problem Statement : Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder : list[int] , postorder : list[int] ):

        if not inorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        inorder_index = inorder.index(root_val)

        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root