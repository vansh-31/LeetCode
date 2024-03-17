# Problem : Bus Routes
# Problem Statement : You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for routes_id, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(routes_id)

        queue = deque([(source, 0)])
        seen_stops = set([source])
        seen_routes = set()
        while queue:
            stop, new_changes = queue.popleft()

            if stop == target:
                return new_changes

            for routes_id in graph[stop]:
                if routes_id not in seen_routes:
                    seen_routes.add(routes_id)

                    for stop in routes[routes_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop, new_changes + 1)) # type: ignore
        return -1
