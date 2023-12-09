# Problem : Binary Tree Inorder Traversal
# Problem Statement : Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    ans.append(curr.val)
                    pred.right = None
                    curr = curr.right
        return ans
