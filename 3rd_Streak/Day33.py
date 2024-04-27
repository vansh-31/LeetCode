# Problem : Freedom Trail
# Problem Statement : In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
# Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.
# Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
from functools import cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R, K = len(ring), len(key)

        @cache
        def dp(r, k):
            if k == K:
                return 0
            char = key[k]
            if ring[r] == char:
                return dp(r, k + 1) + 1
            pos_cw, cnt_cw = r, 0
            while ring[pos_cw] != char:
                pos_cw = pos_cw + 1 if pos_cw < R - 1 else 0
                cnt_cw += 1
            pos_ccw, cnt_ccw = r, 0
            while ring[pos_ccw] != char:
                pos_ccw = pos_ccw - 1 if pos_ccw > 0 else R - 1
                cnt_ccw += 1
            return min(dp(pos_cw, k + 1) + cnt_cw + 1, dp(pos_ccw, k + 1) + cnt_ccw + 1)

        return dp(0, 0)
