# Problem : Minimum Amount of Time to Collect Garbage
# Problem Statement : You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.
# There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.
# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.
# Return the minimum number of minutes needed to pick up all the garbage.
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n, m = len(travel), len(garbage)
        for i in range(1, n):
            travel[i] += travel[i - 1]
        M = P = G = -1
        collect = 0
        for i in range(m):
            if "M" in garbage[i]:
                M = i
            if "P" in garbage[i]:
                P = i
            if "G" in garbage[i]:
                G = i
            collect += len(garbage[i])
        collect += travel[M - 1] if M > 0 else 0
        collect += travel[P - 1] if P > 0 else 0
        collect += travel[G - 1] if G > 0 else 0
        return collect
