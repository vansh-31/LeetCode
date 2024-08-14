# Problem : Find K-th Smallest Pair Distance
# Problem Statement : The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        def check(dist: int) -> bool:
            i = j = cnt = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= dist:
                    cnt += j - i
                    j += 1
            return cnt >= k

        nums.sort()
        n, left, right = len(nums), 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
