# Problem : Find The Original Array of Prefix Xor
# Problem Statement : You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.
# It can be proven that the answer is unique.
from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]