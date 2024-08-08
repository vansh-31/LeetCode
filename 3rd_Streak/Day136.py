# Problem : Spiral Matrix III
# Problem Statement : You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them.
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        drns = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = rows, cols
        nm = n * m
        rslts = []

        def fill(di, y, x, dist):
            while dist > 0:
                rslts.append([y, x])
                y, x = y + drns[di][0], x + drns[di][1]
                dist -= 1

        def walk(di, y, x, ln):
            if di == 0:
                x0 = max(x, 0)
                if 0 <= y < n:
                    fill(di, y, x0, min(x + ln, m) - x0)
                return y, x + ln

            elif di == 1:
                y0 = max(y, 0)
                if 0 <= x < m:
                    fill(di, y0, x, min(y + ln, n) - y0)
                return y + ln, x

            elif di == 2:
                x0 = min(x, m - 1)
                if 0 <= y < n:
                    fill(di, y, x0, x0 - max(x - ln, -1))
                return y, x - ln

            else:
                y0 = min(y, n - 1)
                if 0 <= x < m:
                    fill(di, y0, x, y0 - max(y - ln, -1))
                return y - ln, x

        di = 0
        ln = 1
        y, x = rStart, cStart
        while len(rslts) < nm:
            y, x = walk(di, y, x, ln)
            di = (di + 1) % 4
            if di & 1 == 0:
                ln += 1
        return rslts
