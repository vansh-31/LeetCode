# Problem : Best Time to Buy and Sell Stock with Transaction Fee
# Problem Statement : You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
from functools import cache
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def solve(index,can_buy):
            if index == len(prices):
                return 0
            profit = 0
            if can_buy:
                 profit = max( (-prices[index]) + solve(index + 1, False), solve(index + 1, True))
            else:
                profit = max( prices[index] + solve(index+1,True) - fee, solve(index+1,False) )
            return profit
        return solve(0,True)