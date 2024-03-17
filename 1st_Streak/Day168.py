# Problem : Make Array Strictly Increasing
# Problem Statement : Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
# If there is no way to make arr1 strictly increasing, return -1.
from typing import List
from functools import lru_cache
import math
from bisect import bisect_right
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]):
        @lru_cache(None)
        def dfs(i, prev):
            if i == len(arr1): return 0
            ## Don't change logic
            dont_change = math.inf
            if arr1[i] > prev:
                dont_change = dfs(i+1, arr1[i])
            ## Swap logic
            change = math.inf
            index = bisect_right(arr2, prev)
            if index < len(arr2) and arr2[index] == prev: index += 1
            if index < len(arr2): change = 1 + dfs(i+1, arr2[index])
            return min(change, dont_change)
        arr2.sort()
        ans = dfs(0, -1)
        return ans if ans < math.inf else -1