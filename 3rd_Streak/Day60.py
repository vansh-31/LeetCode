# Problem : Maximum Score Words Formed by Letters
# Problem Statement : Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        count = Counter(letters)

        def useWord(i):
            isValid = True
            earned = 0
            for c in words[i]:
                count[c] -= 1
                if count[c] < 0:
                    isValid = False
                earned += score[ord(c) - ord("a")]
            return earned if isValid else -1

        def unuseWord(i):
            for c in words[i]:
                count[c] += 1

        def dfs(s):
            ans = 0
            for i in range(s, len(words)):
                earned = useWord(i)
                if earned > 0:
                    ans = max(ans, earned + dfs(i + 1))
                unuseWord(i)
            return ans

        return dfs(0)
