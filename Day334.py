# Problem : Minimum One Bit Operations to Make Integers Zero
# Problem Statement : Given an integer n, you must transform it into 0 using the following operations any number of times:
# Change the rightmost (0th) bit in the binary representation of n.
# Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
# Return the minimum number of operations to transform n into 0.
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = bin(n)[2:]
        N, res = len(binary), 0
        for i in range(1, N + 1):
            if binary[-i] == "1":
                res = 2**i - 1 - res
        return res
