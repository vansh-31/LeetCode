# Problem : Remove Zero Sum Consecutive Nodes from Linked List
# Problem Statement : Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0, head)
        d = {0: fake}
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            d[prefix_sum] = head
            head = head.next
        head = fake
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            head.next = d[prefix_sum].next
            head = head.next
        return fake.next
