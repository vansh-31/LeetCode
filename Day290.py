# Problem : Validate Binary Tree Nodes
# Problem Statement : You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.
from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        visited = [False] * n
        root = []
        for i in range(n):
            if visited[i]:
                continue
            queue = [i]
            while queue:
                tmp = queue.pop(0)
                if visited[tmp]:
                    if tmp in root:
                        root.remove(tmp)
                        continue
                    else:
                        return False
                visited[tmp] = True
                if leftChild[tmp] > -1:
                    queue.append(leftChild[tmp])
                if rightChild[tmp] > -1:
                    queue.append(rightChild[tmp])
            root.append(i)
        return len(root) == 1
