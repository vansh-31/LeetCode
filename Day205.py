# Problem : Pow(x, n)
# Problem Statement : Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        N = n
        n = abs(n)
        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1
        return res if N > 0 else 1/res