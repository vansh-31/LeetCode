# Problem : Maximum Value at a Given Index in a Bounded Array
# Problem Statement : You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.
# Note that abs(x) equals x if x >= 0, and -x otherwise.
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        def check(x):
            y = max(0, x - index)
            ans = (x+y) * (x-y+1) // 2
            y = max(0, x - ((n-1) - index))
            ans += (x+y) * (x-y+1) // 2
            return (ans - x)

        l, r = 0, maxSum
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid) <= maxSum:
                l = mid
            else:
                r = mid - 1
        return l + 1