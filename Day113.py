# Problem : Restore The Array
# Problem Statement : A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.
# Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.
from functools import lru_cache
class Solution:
    def numberOfArrays(self, s, k):
        n, mod = len(s), 10**9+7

        @lru_cache(None)
        def dfs(i):
            if i == 0:
                return 1

            total = 0

            for j in range(i-1,-1,-1):
                if s[j] == "0": continue
                elif int(s[j:i]) <= k:
                    total += dfs(j)%mod
                elif int(s[j:i]) > k:
                    break

            return total

        return dfs(n)%mod