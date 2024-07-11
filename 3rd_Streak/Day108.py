# Problem : Reverse Substrings Between Each Pair of Parentheses
# Problem Statement : You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        for ch in s:
            if ch == "(":
                stack.append(ans)
                ans = ""
            elif ch == ")":
                ans = ans[::-1]
                ans = stack.pop() + ans
            else:
                ans += ch
        return ans
