# Problem : Determine if a Cell Is Reachable at a Given Time
# Problem Statement : You are given four integers sx, sy, fx, fy, and a non-negative integer t.
# In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.
# Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.
# A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return False if t == 1 and sx == fx and sy == fy else max((abs(sx - fx)), (abs(sy - fy))) <= t