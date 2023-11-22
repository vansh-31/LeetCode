# Problem : Diagonal Traverse II
# Problem Statement : Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        result = []
        for i in range(m):
            for j in range(len(nums[i])):
                result.append((i + j, m - 1 - i, nums[i][j]))
        return [num for _, _, num in sorted(result)]
