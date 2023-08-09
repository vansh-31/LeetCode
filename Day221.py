# Problem : Minimize the Maximum Difference of Pairs
# Problem Statement : You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        if len(nums) <= 1 or p == 0:
            return 0
        nums.sort()
        def isPossible(x):
            prev,curr,n = 0,1,p
            while curr < len(nums):
                if nums[curr] - nums[prev] <= x:
                    n -= 1
                    curr += 2
                    prev += 2
                else:
                    curr += 1
                    prev += 1
                if n == 0:
                    return True
            return False
        low,high = 0,nums[-1]
        ans = high
        while low <= high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans