# Problem : Find K Pairs with Smallest Sums
# Problem Statement : You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        resV = []
        pq = []

        for x in nums1:
            heapq.heappush(
                pq, [x + nums2[0], 0]
            )
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = (
                pair[0],
                pair[1],
            )

            resV.append([s - nums2[pos], nums2[pos]])

            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1

        return resV


s = Solution()
print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 4))
print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(s.kSmallestPairs([1, 2], [3], 3))
