# Problem : Grumpy Bookstore Owner
# Problem Statement : There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.
class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        n = len(customers)
        satisfied = sum(customers[:minutes])
        satisfied += sum((1 - grumpy[i]) * customers[i] for i in range(minutes, n))
        max_satisfied = satisfied
        for i in range(minutes, n):
            satisfied -= grumpy[i - minutes] * customers[i - minutes]
            satisfied += grumpy[i] * customers[i]
            max_satisfied = max(max_satisfied, satisfied)
        return max_satisfied
