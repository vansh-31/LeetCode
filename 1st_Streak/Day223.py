# Problem : Coin Change II
# Problem Statement : You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [ [-1] * (amount+1) for _ in range(n) ]
        def solve(index,curr_amount ):
            if curr_amount == 0:
                return 1

            if index >= n or curr_amount < 0:
                return 0

            if dp[index][curr_amount ] != -1:
                return dp[index][curr_amount ]

            take = 0
            if curr_amount >= coins[index]:
                take = solve(index, curr_amount - coins[index] )
            not_take = solve(index+1,curr_amount)
            dp[index][curr_amount ] = take + not_take
            return dp[index][curr_amount ]
        return solve(0,amount)