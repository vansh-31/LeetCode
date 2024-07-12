# Problem : Maximum Score From Removing Substrings
# Problem Statement : You are given a string s and two integers x and y. You can perform two types of operations any number of times.
# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeSubstring(s, pair):
            stack = []
            for i in s:
                if stack and stack[-1] + i == pair:
                    stack.pop()
                else:
                    stack.append(i)
            temp = "".join(stack)
            return temp[::-1]

        totalScore = 0
        if x > y:
            highPriority = "ab"
            lowPriority = "ba"
        else:
            highPriority = "ba"
            lowPriority = "ab"

        new1 = removeSubstring(s, highPriority)
        totalScore += ((len(s) - len(new1)) // 2) * max(x, y)
        new2 = removeSubstring(new1, highPriority)
        totalScore += ((len(new1) - len(new2)) // 2) * min(x, y)
        return totalScore
