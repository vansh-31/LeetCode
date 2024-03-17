# Problem : Champagne Tower
# Problem Statement : We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pyramid = [ [0.0 for _ in range(row+1)] for row in range(101) ]
        pyramid[0][0] = poured
        mx = poured
        row = 0
        while mx > 1 and row < 100:
            mx = 0
            for col in range(row+1):
                if pyramid[row][col] <= 1:
                    continue
                x = pyramid[row][col] - 1
                pyramid[row+1][col] += x/2
                pyramid[row+1][col+1] += x/2
                mx = max(mx,pyramid[row+1][col],pyramid[row+1][col+1])
                pyramid[row][col] = 1
            row += 1
        return pyramid[query_row][query_glass]