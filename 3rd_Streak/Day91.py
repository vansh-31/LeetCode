# Problem : Minimum Number of K Consecutive Bit Flips
# Problem Statement : You are given a binary array nums and an integer k.
# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
# A subarray is a contiguous part of an array.
from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        is_flipped = 0
        flip_positions = deque()
        for i in range(n):
            if flip_positions and flip_positions[0] == i:
                flip_positions.popleft()
                is_flipped ^= 1
            if nums[i] == is_flipped:
                if i + k > n:
                    return -1
                flip_positions.append(i + k)
                is_flipped ^= 1
                flips += 1
        return flips
