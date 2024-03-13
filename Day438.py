# Problem : Find the Pivot Integer
# Problem Statement : Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
class Solution:
    def pivotInteger(self, n: int) -> int:
        li,c=[i for i in range(1,n+1)],-1
        for i in range(len(li)):
            if sum(li[0:i+1])==sum(li[i:]):
                c=i+1
        return c