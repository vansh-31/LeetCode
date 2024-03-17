# Problem : Restore the Array From Adjacent Pairs
# Problem Statement : There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.
from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        ans = []

        def dfs(node, parent):
            ans.append(node)
            for nbr in adj[node]:
                if nbr == parent:
                    continue
                dfs(nbr, node)

        for node, nbrs in adj.items():
            if len(nbrs) == 1:
                dfs(node, None)
                break
        return ans
