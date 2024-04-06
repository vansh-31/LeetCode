# Problem : Minimum Remove to Make Valid Parentheses
# Problem Statement : Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = 0
        for c in s:
            if c == "(":
                left += 1
                stack.append("(")
            elif c == ")":
                if left == 0:
                    continue
                left -= 1
                stack.append(")")
            else:
                stack.append(c)
        ans = ""
        while stack:
            c = stack.pop()
            if c == "(" and left > 0:
                left -= 1
                continue
            ans += c
        return ans[::-1]
