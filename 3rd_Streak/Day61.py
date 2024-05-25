# Problem : Word Break II
# Problem Statement : Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        ans = []

        def solve(index, temp):
            nonlocal ans
            if index >= n:
                ans.append(temp[:-1])
                return
            for word in wordDict:
                m = len(word)
                if word == s[index : index + m]:
                    solve(index + m, temp + s[index : index + m] + " ")

        solve(0, "")
        return ans
