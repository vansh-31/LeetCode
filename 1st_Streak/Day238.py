# Problem : Maximum Length of Pair Chain
# Problem Statement : You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort( key= lambda x:(x[-1],-x[0]) )
        x = pairs[0][1]
        ans = 1
        for i in range(1,len(pairs)):
            if x < pairs[i][0]:
                x = pairs[i][1]
                ans += 1
        return ans