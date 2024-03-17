# Problem : Maximum Number of Vowels in a Substring of Given Length
# ProblemStatement : Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        queue = []
        n = len(s)
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
                queue.append(i)
        j = k
        while j < n:
            count = max(count,len(queue))
            if len(queue) > 0 and j - queue[0] >= k:
                queue.pop(0)
            if s[j] in vowels:
                queue.append(j)
            j+=1
        count = max(count,len(queue))
        return count