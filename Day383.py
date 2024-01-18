# Problem : Climbing Stairs
# Problem Statement : You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 1
        curr = 2
        for i in range(3, n + 1):
            curr, prev = curr + prev, curr
        return curr
