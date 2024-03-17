# Problem : Kth Largest Element in an Array
# Problem Statement : Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in range(k,len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap,nums[i])
        return heap[0]