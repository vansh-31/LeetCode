# Problem : Number of Dice Rolls With Target Sum
# Problem Statement : You have n dice, and each die has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7

        @cache
        def solve(dice, x):
            if dice == 0:
                return x == 0
            ans = 0
            for face in range(1, k + 1):
                if x - face >= 0:
                    ans += solve(dice - 1, x - face) % mod
                ans = ans % mod
            return ans % mod

        return solve(n, target) % mod
