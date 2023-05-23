# Problem : Kth Largest Element in a Stream
# Problem Statement : Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k
        self.minn = 999999999
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.minn = min(self.minn,val)
            heapq.heappush(self.heap,val)
        elif val > self.minn:
            self.minn = heapq.heappushpop(self.heap,val)
        return heapq.nsmallest(1,self.heap)[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)