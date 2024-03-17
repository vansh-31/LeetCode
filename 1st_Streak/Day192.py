# Problem : All Nodes Distance K in Binary Tree
# Problem Statement : Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        graph = collections.defaultdict(list)
        def dfs(node):
            if node == None:
                return 
            
            if node.left != None:
                graph[node].append(node.left)
                graph[node.left].append(node)
            
            if node.right != None:
                graph[node].append(node.right)
                graph[node.right].append(node)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        visited = set()
        ans = []
        queue = collections.deque([[target,0]])
        while len(queue) >0:
            node,dist = queue.popleft()
            visited.add(node)
            if dist == k:
                ans.append(node.val)
                continue
            for children in graph[node]:
                if children not in visited:
                    queue.append([children,dist+1])
        return ans