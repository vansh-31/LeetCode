# Problem : Sum of Subarray Minimums
# Problem Statement : Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.
from typing import List
from math import inf


class Solution:
    def sumSubarrayMins(self, A) -> int:
        A = [-inf] + A + [-inf]
        n = len(A)
        st = []
        res = 0
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                mid = st.pop()
                left = st[-1]
                right = i
                res += A[mid] * (mid - left) * (right - mid)
            st.append(i)
        return res % (10**9 + 7)
