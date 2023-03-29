# Problem : Reducing Dishes
# Problem Statement : A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
class Solution:
    def maxSatisfaction(self, sat: list[int]) -> int:
        sat.sort(reverse=True)
        total = 0
        cur_sum = 0
        for val in sat:
            cur_sum += val
            if (cur_sum < 0):
                break
            total += cur_sum
        return total