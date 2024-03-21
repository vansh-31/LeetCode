# Problem : Reverse Linked List
# Problem Statement : Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):
        curr, prev = head, None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
