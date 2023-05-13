# Problem : Count Ways To Build Good Strings
# Problem Statement : Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.

# A good string is a string constructed by the above process having a length between low and high (inclusive).

# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
from collections import Counter
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter({0: 1})
        mod = 10 ** 9 + 7
        for i in range(1, high + 1):
            
            z = dp[i - zero]
            
            o = dp[i - one]
            
            n = (z + o) % mod
           
            dp[i] = n
        
        
        ans = sum(dp[i] for i in range(low, high + 1)) % mod
        
     
        return ans