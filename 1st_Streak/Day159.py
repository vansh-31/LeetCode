# Problem : Count Negative Numbers in a Sorted Matrix
# Problem Statement : Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        totalNegatives = 0
        for row in grid:
            neg = -1
            low,high = 0,len(row)-1
            while low <= high:
                mid = ( low + high )//2
                if row[mid] < 0:
                    neg = mid
                    high = mid-1
                else:
                    low = mid + 1
            if neg != -1:
                totalNegatives += len(row) - neg
        return totalNegatives
s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))