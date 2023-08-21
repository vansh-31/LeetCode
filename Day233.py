# Problem : Repeated Substring Pattern
# Problem Statement : Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(a,b):
            step = len(a)
            n = len(b)
            i = 0
            while i < n:
                if a != b[i:i+step]:
                    return False
                i+=step
            return True
        for i in range(1,len(s)//2+1):
            if check(s[:i],s[i:]):
                return True
        return False