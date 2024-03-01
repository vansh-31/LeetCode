# Problem : Maximum Odd Binary Number
# Problem Statement : You are given a binary string s that contains at least one '1'.
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
# Return a string representing the maximum odd binary number that can be created from the given combination.
# Note that the resulting string can have leading zeros.
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted([x for x in s])[::-1]  # type: ignore
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                s[i], s[-1] = s[-1], s[i]  # type: ignore
                break
        return "".join(s)
