# Problem : Partition Array for Maximum Sum
# Problem Statement : Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int):
        memo = {}

        def solve(curr_idx, curr_cnt, curr_max):
            if (curr_idx, curr_cnt) in memo:
                return memo[(curr_idx, curr_cnt)]
            if curr_cnt > k:
                return float("-inf")
            if curr_idx == len(arr):
                return curr_cnt * curr_max
            not_divide = solve(curr_idx + 1, curr_cnt + 1, max(curr_max, arr[curr_idx]))
            divide = curr_max * curr_cnt + solve(curr_idx + 1, 1, arr[curr_idx])
            memo[(curr_idx, curr_cnt)] = max(not_divide, divide)
            return memo[(curr_idx, curr_cnt)]

        return solve(0, 0, 0)
