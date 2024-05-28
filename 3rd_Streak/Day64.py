# Problem : Get Equal Substrings Within Budget
# Problem Statement : You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        prefix = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        def check(window_size):
            for i in range(n - window_size + 1):
                left = prefix[i - 1] if i > 0 else 0
                right = prefix[i + window_size - 1]
                if right - left <= maxCost:
                    return True
            return False

        low, high = 0, n
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
