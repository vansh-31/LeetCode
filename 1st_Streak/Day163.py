# Problem : Summary Ranges
# Problem Statement : You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        start, end, result = 0, 0, []
    
        while start < len(nums) and end<len(nums):
            if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
                end=end+1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start])+'->'+str(nums[end]))
                    start = end + 1
                    end = end + 1

        return result

s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))