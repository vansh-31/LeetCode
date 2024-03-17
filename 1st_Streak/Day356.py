# Problem : Maximum Score After Splitting a String
# Problem Statement : Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        sum = s.count("1", 1)
        if s[0] == "0":
            sum += 1
        ans = sum
        for c in s[1 : n - 1]:
            if c == "0":
                sum += 1
            else:
                sum -= 1
            ans = max(ans, sum)
        return ans
