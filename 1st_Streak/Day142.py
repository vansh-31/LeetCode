# Problem : Top K Frequent Elements
# Problem Statement : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result