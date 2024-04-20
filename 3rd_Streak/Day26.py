# Problem : Find All Groups of Farmland
# Problem Statement : You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        n=len(land)
        m=len(land[0])
        ans=[]
        for i in range(n):
            for j in range(m):
                if land[i][j]:
                    min_i,min_j=i,j
                    max_i,max_j=i,j
                    stack=[(i,j)]
                    land[i][j]=0
                    while stack:
                        i,j=stack.pop()
                        for x,y in (i-1,j),(i,j-1),(i,j+1),(i+1,j):
                            if 0<=x<n and 0<=y<m and land[x][y]:
                                stack.append((x,y))
                                land[x][y]=0
                                max_i=max(max_i,x)
                                max_j=max(max_j,y)
                    ans.append([min_i,min_j,max_i,max_j])
        return ans