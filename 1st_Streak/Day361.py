# Problem : Minimum Time to Make Rope Colorful
# Problem Statement : Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        l = 0
        removes = 0
        for r in range(n):
            if colors[r] != colors[l]:
                sameColors = neededTime[l:r]
                removes += sum(sameColors) - max(sameColors)
                l = r
        removes += sum(neededTime[l:]) - max(neededTime[l:])
        return removes
