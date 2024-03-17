# Problem : Find the Index of the First Occurrence in a String
# Problem Statement : Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0,len(needle)-1
        while j < len(haystack):
            if haystack[i:j+1]==needle:
                return i
            i+=1
            j+=1
        return -1