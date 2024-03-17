# Problem : Palindrome Partitioning
# Problem Statement : Given a string s, partition s such that every 
# substring of the partition is a palindrome
# Return all possible palindrome partitioning of s.
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        lst = []
        def palindrome(a):
            return a == a[::-1]
        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return 
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    dfs(j+1, curr + [s[i:j+1]])
            return 
        dfs(0,[])
        return lst