# Problem : Image Smoother
# Problem Statement : An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        n, m = len(img), len(img[0])
        fltr = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (0, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        ans = []

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        for i in range(n):
            ans.append([])
            for j in range(m):
                val = 0
                cnt = 0
                for x, y in fltr:
                    I, J = i + x, j + y
                    if isValid(I, J):
                        val += img[I][J]
                        cnt += 1
                ans[-1].append(val // cnt)
        return ans
