# Problem : Find Players With Zero or One Losses
# Problem Statement : You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.
from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        dct = defaultdict(lambda: [0, 0])
        for p1, p2 in matches:
            dct[p1][0] += 1
            dct[p1][1] += 1
            dct[p2][0] += 1
        print(dct)
        wonAll = []
        lossOne = []
        for i in dct:
            if dct[i][0] == dct[i][1]:
                wonAll.append(i)
            elif dct[i][0] - dct[i][1] == 1:
                lossOne.append(i)
        wonAll.sort()
        lossOne.sort()
        return [wonAll, lossOne]
