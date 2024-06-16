# Problem : Patching Array
# Problem Statement : Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
# Return the minimum number of patches required.
class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss, added, index = 1, 0, 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                added += 1
        return added
