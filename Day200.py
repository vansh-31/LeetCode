# Problem : Non-overlapping Intervals
# Problem Statement : Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1] )
        prev = 0
        count = 0
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                count += 1
            else:
                prev = i
        return count