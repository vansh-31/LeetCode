# Problem : Hand of Straights
# Problem Statement : Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    heapq.heappop(heap)
        return True
