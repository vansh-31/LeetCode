# Problem : Maximum Running Time of N Computers
# Problem Statement : You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.
# Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.
# Note that the batteries cannot be recharged.
# Return the maximum number of minutes you can run all the n computers simultaneously.
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort(key=lambda x:-x)
        low,high = batteries[n-1],(sum(batteries) // n) + 1
        ans = 0
        def isPossible(time):
            index = 0
            while index < len(batteries):
                if batteries[index] < time:
                    break
                index += 1
            if n - index <= 0:
                return True
            return sum(batteries[index:])//(n-index) >= time
        while low < high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid
        return ans