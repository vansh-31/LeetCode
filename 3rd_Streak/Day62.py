# Problem : Student Attendance Record II
# Problem Statement : An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def f(i, absent, late):
            if absent >= 2 or late >= 3:
                return 0
            if i == 0:
                return 1
            if dp[i][absent][late] != -1:
                return dp[i][absent][late]
            ans = f(i - 1, absent, 0)
            ans += f(i - 1, absent, late + 1)
            ans += f(i - 1, absent + 1, 0)
            dp[i][absent][late] = ans % mod
            return dp[i][absent][late]

        return f(n, 0, 0)
