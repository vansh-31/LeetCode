# Problem : Open the Lock
# Problem Statement : You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue = deque()
        queue.append("0000")
        visited = set("0000")
        steps = 0
        if "0000" in deadends:
            return -1
        if target == "0000":
            return steps
        while (size := len(queue)) != 0:
            steps += 1
            for i in range(size):
                curr = queue.popleft()
                for wheel in range(4):
                    for move in (1, -1):
                        new_combo = (
                            curr[:wheel]
                            + str((ord(curr[wheel]) - ord("0") + move) % 10)
                            + curr[wheel + 1 :]
                        )
                        if new_combo == target:
                            return steps
                        if new_combo in visited or new_combo in deadends:
                            continue
                        else:
                            visited.add(new_combo)
                            queue.append(new_combo)
        return -1
