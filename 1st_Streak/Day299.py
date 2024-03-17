# Problem : Binary Trees With Factors
# Problem Statement : Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        s = set(arr)
        dp = {x: 1 for x in arr}

        for i in arr:
            for j in arr:
                if j > i**0.5:
                    break
                if i % j == 0 and i // j in s:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    dp[i] %= MOD

        return sum(dp.values()) % MOD
