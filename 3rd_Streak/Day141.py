# Problem : Combination Sum II
# Problem Statement : Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        currset = []
        superset = []

        def solve(i, currset):
            if sum(currset) == target:
                superset.append(currset.copy())
                return

            if (sum(currset) > target) or i >= len(candidates):
                return
            currset.append(candidates[i])
            solve(i + 1, currset)

            currset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            solve(i + 1, currset)

        solve(0, currset)
        return superset
