# Problem : Find the Maximum Sum of Node Values
# Problem Statement : There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.
# Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:
# Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
# nums[u] = nums[u] XOR k
# nums[v] = nums[v] XOR k
# Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
from typing import List
from functools import cache


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        @cache
        def solve(i, c):
            print(i, c)
            if i == n:
                if c == 1:
                    return -(1 << 31)
                return 0
            x = nums[i]
            return max(x + solve(i + 1, c), (x ^ k) + solve(i + 1, 1 - c))

        return solve(0, 0)
