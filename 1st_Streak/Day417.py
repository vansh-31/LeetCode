# Problem : Find the Town Judge
# Problem Statement : In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_count = [0] * (n + 1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        return -1
