# Problem : Remove Nodes From Linked List
# Problem Statement : You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p, head = head, None
        while p:
            t = p.next
            p.next = head
            head = p
            p = t
        p, head.next = head.next, None  # type: ignore
        while p:
            t = p.next
            if head.val <= p.val:  # type: ignore
                p.next = head
                head = p
            p = t
        return head