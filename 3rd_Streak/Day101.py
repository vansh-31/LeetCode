# Problem : Merge Nodes in Between Zeros
# Problem Statement : You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head.next, head.next  # type: ignore
        sum = 0
        while curr:
            x = curr.val
            if x != 0:
                sum += x
            else:
                prev.val = sum  # type: ignore
                prev.next = curr.next
                prev = prev.next  # type: ignore
                sum = 0
            curr = curr.next
        return head.next  # type: ignore
