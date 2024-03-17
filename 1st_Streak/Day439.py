# Problem : Binary Subarrays With Sum
# Problem Statement : Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        sum_counts = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in sum_counts:
                count += sum_counts[prefix_sum - goal]
            sum_counts[prefix_sum] = sum_counts.get(prefix_sum, 0) + 1

        return count
