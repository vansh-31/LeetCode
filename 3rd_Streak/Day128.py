# Problem : Filling Bookcase Shelves
# Problem Statement : You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
# We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
# We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
# Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
from functools import cache
from math import inf
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf: int) -> int:
        N = len(books)

        @cache
        def solve(index=0, height=0, width=shelf):
            if width < 0:
                return inf
            if index == N:
                return height
            x, y = books[index]
            return min(
                solve(index + 1, max(height, y), width - x),
                height + solve(index + 1, y, shelf - x),
            )

        return solve() # type: ignore
