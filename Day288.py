# Problem : Number of Ways to Stay in the Same Place After Some Steps
# Problem Statement : You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.
from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 10**9 + 7

        @cache
        def solve(pos, steps):
            if pos < 0 or pos == arrLen:
                return 0
            if steps == 0:
                return pos == 0
            return (
                (solve(pos, steps - 1) % M)
                + (solve(pos - 1, steps - 1) % M)
                + (solve(pos + 1, steps - 1) % M)
            ) % M

        return solve(0, steps)
