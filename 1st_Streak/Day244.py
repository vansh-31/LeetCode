# Problem : Counting Bits
# Problem Statement : Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
class Solution:
    def countBits(self, n: int) -> list[int]:
        arr = [0] * (n+1)
        def count(x):
            ct = 0
            while x:
                ct += (x & 1)
                x >>= 1
            return ct
        for i in range(n+1):
            arr[i] = count(i)
        return arr