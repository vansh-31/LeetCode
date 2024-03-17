# Problem : Knight Probability in Chessboard
# Problem Statement : On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dp(cur_r,cur_c,k):
            if k==0:
                return 1
            else:
                ans=0
                for r,c in moves:
                    now_r=cur_r+r
                    now_c=cur_c+c
                    if 0<=now_r<=n-1 and 0<=now_c<=n-1:
                        ans+=dp(now_r,now_c,k-1)
                return ans
        if k==0:
            return 1
        moves=[[1,2],[2,1],[1,-2],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]
        return dp(row,column,k)/8**k            