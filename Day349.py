# Problem : Destination City
# Problem Statement : You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
from collections import defaultdict
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str: # type: ignore
        d, p = defaultdict(str), set()
        for i, j in paths:
            d[i] += j
            p.add(i)
            p.add(j)
        for i in p:
            if i not in d.keys(): return i