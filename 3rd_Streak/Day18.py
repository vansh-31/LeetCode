# Problem : Trapping Rain Water
# Problem Statement : Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        leftBigger = height[:]
        rightBigger = height[:]
        mxLeft = height[0]
        mxRight = height[-1]
        for i in range(n):
            if height[i] > mxLeft:
                mxLeft = height[i]
            if height[-1-i] > mxRight:
                mxRight = height[-1-i]
            leftBigger[i] = mxLeft
            rightBigger[-1-i] = mxRight
        ans = 0
        for i in range(n):
            ans += min( leftBigger[i], rightBigger[i] ) - height[i]
        return ans