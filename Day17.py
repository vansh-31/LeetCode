# Problem : Flip String to Monotone Increasing
# Problem Statement : A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        ones, ans = 0, 0                    # Example: s = "010110"
                                            #
        for num in s:                       #  num    ones   ans  
                                            #  ––––   ––––   ––––  
            if num =='1': ones += 1         #    0      0     0
                                            #    1      1     0
            elif ones:                      #    0      0     1
                ones -= 1                   #    1      1     1
                ans += 1                    #    1      2     1
                                            #    0      1     2
        return ans