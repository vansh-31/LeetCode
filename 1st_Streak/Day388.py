# Problem : Maximum Length of a Concatenated String with Unique Characters
# Problem Statement : You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def solve(i, seen):
            if i >= len(arr):
                return 0
            notIncluded = solve(i + 1, seen)
            currSeen = set()
            for c in arr[i]:
                if c in seen or c in currSeen:
                    return notIncluded
                currSeen.add(c)
            included = len(arr[i]) + solve(i + 1, seen | set(arr[i]))
            return max(notIncluded, included)

        return solve(0, set())
