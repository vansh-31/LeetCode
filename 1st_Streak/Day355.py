# Problem : Widest Vertical Area Between Two Points Containing No Points
# Problem Statement : Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_width = 0
        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)
        return max_width
