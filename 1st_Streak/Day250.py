# Problem : Reverse Linked List II
# Problem Statement : Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        nodes = []
        values = []
        pos = 1
        curr = head
        while curr:
            if pos >= left and pos <= right:
                nodes.append(curr)
                values.append(curr.val)
            curr = curr.next
            pos += 1
        for node in nodes:
            node.val = values.pop()
        return head
