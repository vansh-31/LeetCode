# Problem : Reorder List
# Problem Statement : You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque


class Solution:
    def reorderList(self, head: ListNode) -> None:
        q = deque()
        p = head.next
        while p:
            q.append(p)
            p = p.next
        p = head
        while len(q):
            p.next = q.pop()
            p = p.next
            if len(q):
                p.next = q.popleft()
                p = p.next
        p.next = None
