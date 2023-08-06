# Problem : Number of Music Playlists
# Problem Statement : Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:
# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
# Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.
from functools import cache
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        @cache
        def solve( curr_goal , used_songs ):
            if curr_goal == goal:
                return used_songs == n

            # Choose new song
            new_song_choice = (n-used_songs) * solve( curr_goal+1, used_songs+ 1 )%mod

            # Choose old song
            old_song_choice = 0
            if used_songs > k:
                old_song_choice = (used_songs - k ) * solve( curr_goal+1, used_songs ) % mod
            return (new_song_choice + old_song_choice)%mod
        return solve(0,0)