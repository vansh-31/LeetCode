# Problem : Remove K Digits
# Problem Statement : Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        res = stack[:-k] if k else stack
        return "".join(res).lstrip("0") or "0"
