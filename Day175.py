# Problem : Tallest Billboard
# Problem Statement : You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.
# You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.
# Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.
from functools import cache
class Solution:
    def tallestBillboard(self, rods):
        n = len(rods)
        @cache
        def dfs(diff,j):
            if j >= n: return 0 if diff == 0 else float("-inf")
            l = rods[j]
            return max(dfs(diff-l,j+1),dfs(diff+l,j+1) + l,dfs(diff,j+1))
        return dfs(0,0)