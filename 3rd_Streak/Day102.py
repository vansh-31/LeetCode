# Problem : Find the Minimum and Maximum Number of Nodes Between Critical Points
# Problem Statement : A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [0, 0]

        arr = []
        min_d, max_d = float("inf"), -float("inf")
        first_critical, last_critical = None, None
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(1, len(arr) - 1):
            if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (
                arr[i] < arr[i - 1] and arr[i] < arr[i + 1]
            ):
                if last_critical is None:
                    first_critical = last_critical = i
                else:
                    min_d = min(min_d, i - last_critical)
                    max_d = max(max_d, i - first_critical)  # type: ignore
                    last_critical = i
        if min_d == float("inf") or max_d == -float("inf"):
            return [-1, -1]
        return [min_d, max_d]  # type: ignore
