# Problem : Knight Dialer
# Problem Statement : The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:
# A chess knight can move as indicated in the chess diagram below:
# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).
# Given an integer n, return how many distinct phone numbers of length n we can dial.
# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.
# As the answer may be very large, return the answer modulo 109 + 7.
class Solution:
    def knightDialer(self, n: int) -> int:
        arr=[1 for i in range(10)]
        for i in range(n-1):
            arr=[
                arr[4]+arr[6],
                arr[6]+arr[8],
                arr[7]+arr[9],
                arr[4]+arr[8],
                arr[3]+arr[9]+arr[0],
                0,
                arr[1]+arr[7]+arr[0],
                arr[2]+arr[6],
                arr[1]+arr[3],
                arr[2]+arr[4]
                ]
        return sum(arr)%(10**9+7)