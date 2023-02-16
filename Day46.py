# Problem : Add to Array-Form of Integer
# Problem Statement : The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = ''.join([str(elem) for elem in num])
        ans = int(ans)
        ans += k
        ans = str(ans)
        ans = [int(x) for x in ans]
        return ans
        