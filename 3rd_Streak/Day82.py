# Problem : IPO
# Problem Statement : Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
# The answer is guaranteed to fit in a 32-bit signed integer.
from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        cp = list(zip(capital, profits))
        cp.sort()

        pq = []
        curr = 0
        for i in range(k):
            while curr < n and cp[curr][0] <= w:
                heapq.heappush(pq, -cp[curr][1])
                curr += 1
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        return w
