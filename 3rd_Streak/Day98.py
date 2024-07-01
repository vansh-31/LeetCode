# Problem : Three Consecutive Odds
# Problem Statement : Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for x in arr:
            if x & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
