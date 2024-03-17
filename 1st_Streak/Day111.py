# Problem : Profitable Schemes
# Problem Statement :  There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.
# Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.
# Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        dp = [[[-1 for x in range(minProfit+1)] for y in range(n+1)] for z in range(len(group)+1)]
        def solve(i,n,minProfit):
            if n < 0:
                return 0
            if i >= len(group):
                if minProfit>0:
                    return 0
                return 1
            if dp[i][n][minProfit] != -1:
                return dp[i][n][minProfit]
            not_take = solve(i+1,n,minProfit)
            take = 0
            if minProfit-profit[i]<0:
                take = solve(i+1,n-group[i],0)
            else:
                take = solve(i+1,n-group[i],minProfit-profit[i])
            dp[i][n][minProfit] =( (take%1000000007) + (not_take%1000000007) )%1000000007
            return dp[i][n][minProfit]
        return solve(0,n,minProfit)