# Problem : Optimal Partition of String
# Problem Statement : Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        sub = ""
        for i in range(len(s)):
            if s[i] in sub:
                ans +=1
                sub = ""
            sub += s[i]
        return ans+1