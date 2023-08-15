# Problem : Partition List
# Problem Statement : Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessT_than = []
        greater_than_or_equalt = []
        curr = head
        while curr:
            if curr.val < x:
                lessT_than.append(curr.val)
            else:
                greater_than_or_equalt.append(curr.val)
            curr = curr.next
        curr = head
        i = 0
        while i < len(lessT_than):
            curr.val = lessT_than[i]
            i += 1
            curr = curr.next

        i = 0
        while i < len(greater_than_or_equalt):
            curr.val = greater_than_or_equalt[i]
            i += 1
            curr = curr.next
        return curr
