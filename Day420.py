# Problem : Greatest Common Divisor Traversal
# Problem Statement : You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
# Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
# Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
from typing import List
from math import isqrt
from collections import defaultdict


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        par = {i: i for i in range(n)}
        rank = {j: j for j in range(n)}

        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return 1

        def getPrimeDivs(n):
            if n < 0:
                return []
            ans = set()
            for i in range(2, isqrt(n) + 1):
                while n % i == 0:
                    ans.add(i)
                    n //= i
            if n > 1:
                ans.add(n)
            return ans

        primes = defaultdict(list)
        for idx, i in enumerate(nums):
            primesDivs = getPrimeDivs(i)
            for p in primesDivs:
                primes[p].append(idx)
        for p in primes:
            for i in primes[p]:
                union(i, primes[p][0])
        return sum(i == find(i) for i in range(n)) == 1
