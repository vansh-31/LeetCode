# Problem : Balance a Binary Search Tree
# Problem Statement : Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        In = []
        curr = root
        while curr:
            if not curr.left:
                In.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if pred.right == None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    In.append(curr.val)
                    curr = curr.right

        def createBST(st, end):
            if st > end:
                return None
            mid = (st + end) // 2
            root = TreeNode(In[mid])
            root.left = createBST(st, mid - 1)
            root.right = createBST(mid + 1, end)
            return root

        return createBST(0, len(In) - 1)  # type: ignore
