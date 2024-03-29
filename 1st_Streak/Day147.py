# Problem : Stone Game III
# Problem Statement : Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.
# The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.
# The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.
# Assume Alice and Bob play optimally.
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * 3

        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[(i + 1) % 3]
            take_two = float('-inf')
            if i + 1 < n:
                take_two = stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 3]
            take_three = float('-inf')
            if i + 2 < n:
                take_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 3]

            dp[i % 3] = max(take_one, take_two, take_three)  # type: ignore

        score_diff = dp[0]
        if score_diff > 0:
            return "Alice"
        elif score_diff < 0:
            return "Bob"
        else:
            return "Tie"