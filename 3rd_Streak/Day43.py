# Problem : Double a Number Represented as a Linked List
# Problem Statement : You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
# Return the head of the linked list after doubling it.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            curr, prev = head, None
            while curr:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            return prev

        head = rev(head)
        carry = 0
        curr = head
        while curr:
            dig = 2 * curr.val
            curr.val = (dig % 10) + carry
            carry = dig // 10
            curr = curr.next
        head = rev(head)
        if carry != 0:
            temp = ListNode(carry)
            temp.next = head
            head = temp
        return head
