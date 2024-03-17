# Problem : Find Smallest Letter Greater Than Target
# Problem Statement : You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low,high = 0,len(letters) - 1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if ord( letters[mid] ) > ord( target ):
                ans = letters[mid]
                high = mid-1
            else:
                low = mid+1
        return ans if ans != -1 else letters[0]