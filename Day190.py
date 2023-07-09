# Problem : Substring With Largest Variance
# Problem Statement : The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
# Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def largestVariance(self, s: str) -> int:
        def solveOne(a, b, string):
            max_var = 0
            var = 0
            has_b = False
            first_b = False
            for c in string:
                if c == a:
                    var += 1
                elif c == b:
                    has_b = True
                    if first_b and var >= 0:
                        first_b = False 
                    elif (var - 1) < 0: 
                        first_b = True 
                        var = -1
                    else:
                        var -= 1
                if has_b and var > max_var:
                    max_var = var
            return max_var
        max_variance = 0
        unique = list(set(s))
        for a in unique:
            for b in unique:
                if a == b:
                    continue
                a_against_b_var = solveOne(a, b, s) 
                max_variance = max(a_against_b_var, max_variance)
        return max_variance 