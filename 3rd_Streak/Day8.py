# Problem : Isomorphic Strings
# Problem Statement : Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if (ch1 in m1 and m1[ch1] != ch2) or (ch2 in m2 and m2[ch2] != ch1):
                return False
            m1[ch1] = ch2
            m2[ch2] = ch1
        return True
