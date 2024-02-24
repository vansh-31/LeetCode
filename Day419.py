# Problem : Find All People With Secret
# Problem Statement : You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        q = [(0, 0), (0, firstPerson)]
        graph = defaultdict(list)
        for person_i, person_ii, time in meetings:
            graph[person_i].append((person_ii, time))
            graph[person_ii].append((person_i, time))
        answer = set()
        while q:
            time, person_i = heappop(q)
            if person_i in answer:
                continue
            answer.add(person_i)
            for person_ii, meeting_time in graph[person_i]:
                if meeting_time >= time:
                    heappush(q, (meeting_time, person_ii))
        return list(answer)
