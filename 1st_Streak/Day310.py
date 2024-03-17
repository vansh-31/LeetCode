# Problem : Seat Reservation Manager
# Problem Statement : Design a system that manages the reservation state of n seats that are numbered from 1 to n.
# Implement the SeatManager class:
# SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
# int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
# void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
from heapq import heappush, heappop


class SeatManager:
    def __init__(self, n: int):
        self.last = 0
        self.pq = []

    def reserve(self) -> int:
        if not self.pq:
            self.last += 1
            return self.last
        return heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
