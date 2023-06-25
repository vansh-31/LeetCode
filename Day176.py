# Problem : Count All Possible Routes
# Problem Statement : You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.
# At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.
# Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).
# Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.
from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        Mod=10**9+7
        n=len(locations)
        row=[-1]*(fuel+1)
        dp=[row[:] for _ in range(n)]

        def dfs(i, finish, fuel):
            if fuel<0: return 0
            if dp[i][fuel]!=-1: return dp[i][fuel]
            ans=0
            if i==finish: ans+=1
            for j in range(n):
                if j==i: continue
                ans=(ans+dfs(j, finish, fuel-abs(locations[i]-locations[j])))%Mod
            dp[i][fuel]=ans
            return ans
        return dfs(start, finish, fuel)