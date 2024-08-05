# Problem : Kth Distinct String in an Array
# Problem Statement : A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        hashmap = {}
        for string in arr:
            if string in hashmap:
                hashmap[string] = False
            else:
                hashmap[string] = True
        for key, val in hashmap.items():
            if val:
                k -= 1
                if k == 0:
                    return key
        return ""
