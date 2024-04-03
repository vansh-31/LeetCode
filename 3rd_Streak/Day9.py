# Problem : Word Search
# Problem Statement : Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def isPossible(row, col, ch):
            return (
                0 <= row < m
                and 0 <= col < n
                and ch == board[row][col]
                and not vis[row][col]
            )

        def solve(row, col, index):
            if index == len(word):
                return True
            ch = word[index]
            vis[row][col] = True
            ans = False
            if isPossible(row + 1, col, ch):
                ans |= solve(row + 1, col, index + 1)
            if isPossible(row - 1, col, ch):
                ans |= solve(row - 1, col, index + 1)
            if isPossible(row, col + 1, ch):
                ans |= solve(row, col + 1, index + 1)
            if isPossible(row, col - 1, ch):
                ans |= solve(row, col - 1, index + 1)
            vis[row][col] = False
            return ans

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if len(word) == 1:
                        return True
                    vis[row][col] = True
                    if solve(row, col, 1):
                        return True
                    vis[row][col] = False
        return False
