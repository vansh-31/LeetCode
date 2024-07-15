# Problem : Create Binary Tree From Descriptions
# Problem Statement : You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.


# The test cases will be generated such that the binary tree is valid.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        children = set()
        for parent, child, isLeft in descriptions:
            parentNode = nodes.setdefault(parent, TreeNode(val=parent))
            childNode = nodes.setdefault(child, TreeNode(val=child))
            children.add(child)
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        for node in nodes:
            if node not in children:
                return nodes[node]
