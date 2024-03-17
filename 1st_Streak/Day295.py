# Problem : Maximum Score of a Good Subarray
# Problem Statement : You are given an array of integers nums (0-indexed) and an integer k.
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
# Return the maximum possible score of a good subarray.
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = k
        mini = nums[k]
        ans = mini
        while left > 0 or right < n - 1:
            if left > 0 and right < n - 1:
                if nums[left - 1] >= nums[right + 1]:
                    left -= 1
                else:
                    right += 1
            elif left > 0:
                left -= 1
            elif right < n - 1:
                right += 1
            mini = min(mini, nums[left], nums[right])
            ans = max(ans, mini * (right - left + 1))
        return ans
