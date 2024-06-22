# Problem : Count Number of Nice Subarrays
# Problem Statement : Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res = count = l = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                k -= 1
                count = 0
            while not k:
                k += nums[l] % 2
                count += 1
                l += 1
            res += count
        return res
