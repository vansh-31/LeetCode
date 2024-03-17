# Problem : Check If It Is a Straight Line
# Problem Statement : You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        for i in range(len(coordinates)-1):
            if (abs(coordinates[i][0] - coordinates[i+1][0]) != 1) or (abs(coordinates[i][1] - coordinates[i+1][1]) != 1):
                return False
        return True