# Problem : Fair Distribution of Cookies
# Problem Statement : You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
# Return the minimum unfairness of all distributions.
from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int):
        dp = {}
        def solve(index,childrens):
            if index == len(cookies):
                return max(childrens)
            if childrens.count(0) > len(cookies) - index:
                return float("inf")
            if (index,tuple(childrens)) in dp:
                return dp[(index,tuple(childrens))]
            ans = float("inf")
            for i in range(k):
                childrens[i] += cookies[index]
                ans = min(ans, solve(index + 1,childrens))
                childrens[i] -= cookies[index]
            dp[(index,tuple(childrens))] = ans
            return dp[(index,tuple(childrens))]
        childrens = [0] * k
        return solve(0,childrens)
print(Solution().distributeCookies([8,15,10,20,8],2))