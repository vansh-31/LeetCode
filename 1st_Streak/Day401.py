# Problem : First Unique Character in a String
# Problem Statement : Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        for index, ch in enumerate(s):
            if count[ord(ch) - 97] == 1:
                return index
        return -1
