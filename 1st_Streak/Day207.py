# Problem : Minimum Speed to Arrive on Time
# Problem Statement : You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        if n-1 >= hour:
            return -1
        last = dist[-1]
        dist.sort()
        def check(speed):
            time = 0
            for i in range(n):
                time += math.ceil(dist[i]/speed)
            time -= math.ceil(last/speed)
            time += last/speed
            return time <= hour
        ans = -1
        low,high = 1,dist[-1]
        temp = hour - int(hour)
        if temp != 0:
            while temp < 1:
                temp = temp * 10
                high = high * 10
        while low <= high:
            mid = (low+high)//2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid+1
        return ans