# Problem : Sum of Square Numbers
# Problem Statement : Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c**0.5) + 1
        while low <= high:
            mid = (low**2) + (high**2)
            if mid == c:
                return True
            if mid > c:
                high -= 1
            else:
                low += 1
        return False
