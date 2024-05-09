# Problem : Maximize Happiness of Selected Children
# Problem Statement : You are given an array happiness of length n, and a positive integer k.
# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        sub = ans = 0
        for i in range(n - 1, n - k - 1, -1):
            happiness[i] += sub
            sub -= 1
            ans += max(0, happiness[i])
        return ans
