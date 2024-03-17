# Problem : Sign of the Product of an Array
# Problem Statement : There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).
from functools import reduce
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        ans = reduce(lambda x,y:x*y,nums)
        if ans > 0:
            return 1
        return -1