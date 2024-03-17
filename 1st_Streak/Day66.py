# Problem : Minimum Time to Complete Trips
# Problem Statement : You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        
        st,end = 1,max(time)*totalTrips
        ans = end
        
        def check(givenTime):
            possibleTrips = 0
            for t in time:
                possibleTrips += givenTime//t
            return possibleTrips >=totalTrips
        
        while st<=end:
            mid = (st+end)//2
            if check(mid):
                ans = mid
                end = mid-1
            else:
                st = mid+1
        return ans
    
s = Solution()
n,m = input().split()
n,m = int(n),int(m)
arr = list(map(int,input().split()))
print(s.minimumTime(arr,m))