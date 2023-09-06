# Problem : Split Linked List in Parts
# Problem Statement : Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1
        res = []
        x = n // k
        y = n % k
        curr = head
        for i in range(k):
            length = x if y <= 0 else x + 1
            y -= 1
            if length == 0:
                res.append(None)
                continue
            res.append(curr)
            for j in range(length - 1):
                curr = curr.next
            nextt = curr.next
            curr.next = None
            curr = nextt
        return res
