# Problem : Sliding Window Maximum
# Problem Statement : You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(heap, (-nums[i],i) )
        ans = [-heap[0][0]]
        for i in range(k,n):
            # remove out of range elements or smaller than the current element
            while heap and ( heap[0][1] < (i-k+1) or ( (-heap[0][0]) < nums[i] ) ):
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i],i) )
            ans.append( -heap[0][0] )
        return ans