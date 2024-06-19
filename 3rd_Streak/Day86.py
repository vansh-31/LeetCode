# Problem : Minimum Number of Days to Make m Bouquets
# Problem Statement : You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def isPossible(maxDays):
            bouquets = flowers = 0
            for index, day in enumerate(bloomDay):
                if day <= maxDays:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets == m:
                    return True
            return False

        low, hi = 1, max(bloomDay)
        ans = -1
        while low <= hi:
            mid = low + (hi - low) // 2
            if isPossible(mid):
                ans = mid
                hi = mid - 1
            else:
                low = mid + 1
        return ans
