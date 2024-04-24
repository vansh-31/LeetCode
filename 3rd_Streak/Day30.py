# Problem : Tribonacci Number
# Problem Statement : The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return int(not n == 0)
        zero = 0
        one = two = 1
        for _ in range(3, n + 1):
            temp = zero + one + two
            zero = one
            one = two
            two = temp
        return two
