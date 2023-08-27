# Problem : Frog Jump
# Problem Statement : A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
from functools import cache
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        m = {}
        for i in range(n):
            m[stones[i]] = i
        @cache
        def solve(index,k):
            if index >= n-1:
                return index == n - 1
            can_reach = False
            curr_pos = stones[index]
            k0,kk,k1 = curr_pos+k-1,curr_pos+k,curr_pos+k+1
            if k0 > curr_pos and m.get(k0) != None:
                can_reach = can_reach or solve( m[k0],k-1 )
            if kk > curr_pos and m.get(kk) != None:
                can_reach = can_reach or solve( m[kk],k )
            if m.get(k1) != None:
                can_reach = can_reach or solve( m[k1],k+1 )
            return can_reach
        return solve(0,0)
