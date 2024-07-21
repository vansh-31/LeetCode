# Problem : Build a Matrix With Conditions
# Problem Statement : You are given a positive integer k. You are also given:
# a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
# a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
# The two arrays contain integers from 1 to k.
# You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.
# The matrix should also satisfy the following conditions:
# The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
# The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
# Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
from typing import List
from collections import deque, defaultdict


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topsort(arr):
            g = defaultdict(list)
            in_degree = defaultdict(int)
            ans = []
            for a, b in arr:
                g[a].append(b)
                in_degree[b] += 1
            q = deque()
            for i in range(1, k + 1):
                if i not in in_degree:
                    q.append(i)
            while q:
                curr = q.popleft()
                ans.append(curr)
                for n in g[curr]:
                    in_degree[n] -= 1
                    if in_degree[n] == 0:
                        q.append(n)
            return ans if len(ans) == k else []

        row_order = topsort(rowConditions)
        col_order = topsort(colConditions)
        if not row_order or not col_order:
            return []
        ans = [[0] * k for i in range(k)]
        r = {row_order[i]: i for i in range(k)}
        c = {col_order[i]: i for i in range(k)}
        for i in range(1, k + 1):
            y, x = r[i], c[i]
            ans[y][x] = i
        return ans
