# Problem : Combinations
# Problem Statement : Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(start,remaining,temp):
            nonlocal ans
            if remaining == 0:
                ans.append( temp[:] )
                return
            if start > n:
                return
            for num in range(start,n+1):
                temp.append(num)
                solve(num+1,remaining-1,temp)
                temp.pop()
        solve(1,k,[])
        return ans