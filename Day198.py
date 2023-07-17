# Problem : Add Two Numbers II
# Problem Statement : You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev,curr = None,head
            while curr:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        head = ListNode(-1)
        tail = head
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = val1 + val2 + carry
            tail.next = ListNode( (val%10) )
            tail = tail.next
            carry = val//10
        temp = head
        head = head.next
        del temp
        return reverse(head)