# Problem : Number of Good Pairs
# Problem Statement : Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
from collections import defaultdict
from functools import cache
from typing import List
<<<<<<< HEAD
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
=======


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        @cache
        def fact(x):
            if x <= 1:
                return 1
            return x * fact(x - 1)

        @cache
        def Ncr(N, r):
            return fact(N) // (fact(N - r) * fact(r))

>>>>>>> f025d422fcfb9dad3e03e9f84ade36562664e52f
        vals = defaultdict(int)
        for x in nums:
            vals[x] += 1
        ans = 0
        for x in vals.values():
            if x >= 2:
<<<<<<< HEAD
                ans += comb(x,2)
        return ans
=======
                print(x, Ncr(x, 2))
                ans += Ncr(x, 2)
        return ans
>>>>>>> f025d422fcfb9dad3e03e9f84ade36562664e52f
