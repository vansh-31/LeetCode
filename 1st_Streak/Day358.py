# Problem : Minimum Changes To Make Alternating Binary String
# Problem Statement : You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.
class Solution:
    def minOperations(self, s: str) -> int:
        prev_0 = "1"
        prev_1 = "0"
        oper_0 = 0
        oper_1 = 0
        for b in s:
            if b == prev_1:
                oper_1 += 1
                prev_1 = "1" if b == "0" else "0"
            else:
                prev_1 = b
            if b == prev_0:
                oper_0 += 1
                prev_0 = "1" if b == "0" else "0"
            else:
                prev_0 = b

        return min(oper_1, oper_0)
