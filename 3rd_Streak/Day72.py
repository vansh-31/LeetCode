# Problem : Find Common Characters
# Problem Statement : Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count = [0] * 26
        for ch in words[0]:
            count[ord(ch) - 97] += 1
        for word in words[1:]:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - 97] += 1
            for i in range(26):
                count[i] = min(count[i], temp[i])
        ans = []
        for i in range(26):
            while count[i]:
                ans.append(chr(97 + i))
                count[i] -= 1
        return ans
