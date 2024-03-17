# Problem : Minimum Number of Taps to Open to Water a Garden
# Problem Statement : There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
# There are n + 1 taps located at points [0, 1, ..., n] in the garden.
# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
# Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n+1)
        for i in range(len(ranges)):
            low = max(0,i-ranges[i])
            high = min(n, ranges[i]+i)
            if ranges[i] != 0:
                arr[low] = max(arr[low], high)

        dic = {}
        def helper(index) -> int:
            if index == n:
                return 1
            if index in dic:
                return dic[index]
            ans = float("inf")
            start = index+1
            end = min(index+arr[index]+1,len(arr))
            farthest = arr[index]
            if farthest == n:
                dic[index] = 1
                return 1
            for i in range(start, end):
                if farthest - i < 0:
                    ans = min(ans+1,float("inf"))
                    dic[index] = ans
                    return dic[index]
                if farthest < arr[i]:
                    ans = min(helper(i), ans)
            dic[index] = ans+1
            return int(ans+1)

        v = helper(0)
        if v == float("inf"):
            return -1
        return v