# Problem : Find Unique Binary String
# Problem Statement : Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = int(nums[i], 2)
        nums.sort()
        print(nums)
        ans = None
        for i in range(n):
            if nums[i] != i:
                ans = bin(i)[2:]
                break
        if not ans:
            ans = bin(n)[2:]
        ans = "0" * (n - len(ans)) + ans
        return ans
