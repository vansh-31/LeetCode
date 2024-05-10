# Problem : Kth Smallest Prime Fraction
# Problem Statement : You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int):
        li = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                li.append(arr[i] / arr[j])
        li.sort()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] / arr[j] == li[k - 1]:
                    return [arr[i], arr[j]]
