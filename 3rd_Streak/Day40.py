# Problem : Boats to Save People
# Problem Statement : You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        n = len(people)
        people.sort()
        st, end = 0, n - 1
        boats = 0
        while st <= end:
            if people[st] + people[end] <= limit:
                st += 1
            end -= 1
            boats += 1
        return boats
