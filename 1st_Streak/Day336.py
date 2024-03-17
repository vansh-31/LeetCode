# Problem : Find Words That Can Be Formed by Characters
# Problem Statement : You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = [0] * 26
        for ch in chars:
            count[ord(ch) - 97] += 1
        ans = 0
        for word in words:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - 97] += 1
                if temp[ord(ch) - 97] > count[ord(ch) - 97]:
                    break
            else:
                ans += len(word)
        return ans
