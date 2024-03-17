# Problem : Sort Characters By Frequency
# Problem Statement : Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        answerString = ""
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1
        hashMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        for char, freq in hashMap:
            answerString = f"{answerString}{char*freq}"
        return answerString
