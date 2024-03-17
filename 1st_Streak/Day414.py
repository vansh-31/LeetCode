# Problem : Meeting Rooms III
# Problem Statement : You are given an integer n. There are n rooms numbered from 0 to n - 1.
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
# Meetings are allocated to rooms in the following manner:
# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
# A half-closed interval [a, b) is the interval between a and b including a and not including b.

from heapq import heappush, heappop, heapify


class Solution:
    def mostBooked(self, num_rooms, meetings):
        available_rooms = [room for room in range(num_rooms)]
        occupied_rooms = []
        heapify(available_rooms)
        booking_counts = [0] * num_rooms
        sorted_meetings = sorted(meetings, key=lambda x: x[0])
        for start_time, end_time in sorted_meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                end, room = heappop(occupied_rooms)
                heappush(available_rooms, room)
            if available_rooms:
                room = heappop(available_rooms)
                heappush(occupied_rooms, [end_time, room])
            else:
                current_end, room = heappop(occupied_rooms)
                new_end = current_end + end_time - start_time
                heappush(occupied_rooms, [new_end, room])
            booking_counts[room] += 1
        max_booking_count = max(booking_counts)
        most_booked_room = booking_counts.index(max_booking_count)
        return most_booked_room
