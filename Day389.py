# Problem : Pseudo-Palindromic Paths in a Binary Tree
# Problem Statement :Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        ans = 0

        def search(node, even):
            if node == None:
                return
            even[node.val] = not even[node.val]
            if node.left == None and node.right == None:
                if sum(even) <= 1:
                    nonlocal ans
                    ans += 1
            else:
                search(node.left, even)
                search(node.right, even)
            even[node.val] = not even[node.val]

        search(root, [False] * 10)
        return ans
