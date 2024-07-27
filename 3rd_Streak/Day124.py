# Problem : Minimum Cost to Convert String I
# Problem Statement : You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ):
        n = len(source)
        INF = float("inf")
        NUM_LETTERS = 26
        dist = [[INF] * NUM_LETTERS for _ in range(NUM_LETTERS)]
        for i in range(NUM_LETTERS):
            dist[i][i] = 0
        for o, c, z in zip(original, changed, cost):
            dist[ord(o) - ord("a")][ord(c) - ord("a")] = min(
                dist[ord(o) - ord("a")][ord(c) - ord("a")], z
            )
        for k in range(NUM_LETTERS):
            for i in range(NUM_LETTERS):
                for j in range(NUM_LETTERS):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord("a")
            t_idx = ord(t_char) - ord("a")
            if dist[s_idx][t_idx] == INF:
                return -1
            total_cost += dist[s_idx][t_idx]
        return total_cost
