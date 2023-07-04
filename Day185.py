# Problem : Single Number II
# Problem Statement : Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(32):
            print("----------")
            count = 0
            for n in nums:
                temp = n >> i
                temp = temp & 1
                # print(temp)
                count += temp
            rem = count % 3
            # print("REM:",rem)
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res = res | rem << i
            # print("RES:",res)
        return res