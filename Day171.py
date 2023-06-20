# Problem : K Radius Subarray Averages
# Problem Statement : You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
# For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1
        if n < window_size:
            return avgs
        window = nums[k]
        for i in range(1, k + 1):
            window += nums[k + i] + nums[k - i]
        avgs[k] = window // window_size
        for i in range(k + 1, n - k):
            window += nums[i + k] - nums[i - k - 1]
            avgs[i] = window // window_size
        return avgs