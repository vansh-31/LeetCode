# Problem : Remove Duplicate Letters
# Problem Statement : Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {ch: index for index, ch in enumerate(s)}
        seen = defaultdict(bool)
        stack = []
        for index, ch in enumerate(s):
            if not seen[ch]:
                while stack and ch < stack[-1] and index < last_occ[stack[-1]]:
                    seen[stack[-1]] = False
                    stack.pop()
                seen[ch] = True
                stack.append(ch)
        return "".join(stack)
