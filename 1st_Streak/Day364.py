# Problem : Redistribute Characters to Make All Strings Equal
# Problem Statement : You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        if n == 1:
            return True
        freq = [0] * 26
        for s in words:
            for c in s:
                freq[ord(c) - 97] += 1
        for f in freq:
            if f % n != 0:
                return False
        return True
