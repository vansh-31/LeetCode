# Problem : Swap Nodes in Pairs
# Problem Statement : Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head) -> ListNode:
        def solve(head) -> ListNode:
            if not head:
                return None
            forward = None
            curr = head
            prev = None
            i = 0
            while i < 2 and curr != None:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
                i+=1
            if forward:
                head.next = solve(forward)
            return prev
        return solve(head)