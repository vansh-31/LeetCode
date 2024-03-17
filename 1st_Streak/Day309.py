# Problem : Find the Winner of an Array Game
# Problem Statement : Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game
# It is guaranteed that there will be a winner of the game.
from collections import deque


class Solution:
    def getWinner(self, arr, k: int) -> int:
        arr = deque(arr)
        x = arr.popleft()
        winner = -1
        win_count = 0
        if x > arr[0]:
            winner = x
        else:
            winner = arr.popleft()
            arr.appendleft(x)
        while True:
            contender = arr.popleft()
            if winner > contender:
                win_count += 1
                arr.append(contender)
            else:
                arr.append(winner)
                winner = contender
                win_count = 1
            if win_count == k or win_count > len(arr):
                return winner
        return 0
