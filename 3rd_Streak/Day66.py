# Problem : Count Triplets That Can Form Two Arrays of Equal XOR
# Problem Statement : Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.
class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            x = arr[i]
            for j in range(i + 1, len(arr)):
                x ^= arr[j]
                if x == 0:
                    ans += j - i
        return ans
