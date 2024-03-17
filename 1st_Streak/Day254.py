# Problem : Group the People Given the Group Size They Belong To
# Problem Statement : There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, x in enumerate(groupSizes):
            groups[x].append(i)
        ans = []
        for size, people in groups.items():
            temp = []
            for i in range(len(people)):
                temp.append(people[i])
                if len(temp) == size:
                    ans.append(temp[:])
                    temp.clear()
        return ans
