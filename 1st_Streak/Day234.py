# Problem : Excel Sheet Column Title
# Problem Statement : Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            rem = (columnNumber-1)%26
            columnNumber = (columnNumber-1)//26
            res = chr(65+rem) + res
        return res