from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st,end = 1,max(piles)
        ans = end
        def isPossible(speed):
            totalHours = 0
            for p in piles:
                totalHours += ceil(p/speed)
            return totalHours<=h
        while st<= end:
            mid = (st+end)//2
            if isPossible(mid):
                ans = mid
                end = mid-1
            else:
                st = mid+1
        return ans