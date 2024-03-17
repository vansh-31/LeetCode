# Problem : Kth Missing Positive Number
# Problem Statement : Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        i = 0
        while k > 0:
            i+=1
            if i in arr:
                continue
            k-=1
        return i