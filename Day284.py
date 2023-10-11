# Problem : Number of Flowers in Full Bloom
# Problem Statement : You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.
# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]