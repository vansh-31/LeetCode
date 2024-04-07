# Problem : Valid Parenthesis String
# Problem Statement : Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin,leftMax = 0,0
        for c in s:
            if c=='(':
                leftMin+=1
                leftMax+=1
            elif c ==')':
                leftMin-=1
                leftMax-=1
            else:
                leftMin-=1
                leftMax+=1
            if leftMax<0:
                return False
            leftMin = max(0,leftMin)
        return leftMin==0