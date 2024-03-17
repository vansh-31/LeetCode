# Problem : Largest 3-Same-Digit Number in String
# Problem Statement : You are given a string num representing a large integer. An integer is good if it meets the following conditions:
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
# Note:
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = [-1] * 3
        for i in range(len(num) - 2):
            if int(num[i]) > ans[0] and num[i] == num[i + 1] == num[i + 2]:
                ans = [int(num[i])] * 3
        if ans[0] == -1:
            return ""
        return "".join([str(x) for x in ans])
