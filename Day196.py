# Problem : Maximum Number of Events That Can Be Attended II
# Problem Statement : You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
# Return the maximum sum of values that you can receive by attending events.
from typing import List
from functools import cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort( key = lambda event : (event[1], -event[2]) )
        @cache
        def solve(index,start,k):
            if index == len(events) or k == 0:
                return 0
            attend = 0
            if events[index][0] >= start:
                attend = events[index][2] + solve(index+1,events[index][1]+1,k-1)
            not_attend = solve(index+1,start,k)
            return max( attend,not_attend )
        return solve(0,1,k)