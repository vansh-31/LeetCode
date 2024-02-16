# Problem : Least Number of Unique Integers after K Removals
# Problem Statement : Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        mp = defaultdict(int)
        for x in arr:
            mp[x] += 1
        elements = sorted(mp.items(), key=lambda x: x[1])
        for key, value in elements:
            if value <= k:
                k -= value
                del mp[key]
            else:
                break
        return len(mp)
