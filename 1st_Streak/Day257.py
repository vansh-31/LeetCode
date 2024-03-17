# Problem : Reconstruct Itinerary
# Problem Statement : You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.flight_graph = defaultdict(list)
        self.itinerary = []

    def dfs(self, airport: str) -> None:
        destinations = self.flight_graph[airport]
        while destinations:
            next_destination = destinations.pop()
            self.dfs(next_destination)
        self.itinerary.append(airport)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            from_airport, to_airport = ticket
            self.flight_graph[from_airport].append(to_airport)
        for destinations in self.flight_graph.values():
            destinations.sort(reverse=True)
        self.dfs("JFK")
        self.itinerary.reverse()
        return self.itinerary
