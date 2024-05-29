# Problem : Number of Steps to Reduce a Number in Binary Representation to One
# Problem Statement : Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
# If the current number is even, you have to divide it by 2.
# If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.
class Solution:
    def numSteps(self, s: str) -> int:
        value = int(s, 2)
        steps = 0
        while value > 1:
            if value & 1:
                value += 1
            else:
                value //= 2
            steps += 1
        return steps
