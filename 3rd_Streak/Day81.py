# Problem : Minimum Increment to Make Array Unique
# Problem Statement : You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        mini, maxi = min(nums), max(nums)
        n = len(nums)
        freq = [0] * (maxi + n)
        for x in nums:
            freq[x] += 1

        cnt, inc = 0, 0
        x = mini
        for x in range(mini, n + maxi):
            f = freq[x]
            cnt += f != 0
            if f <= 1:
                continue
            freq[x + 1] += f - 1
            inc += f - 1
            if cnt >= n - 1:
                break
        return inc
