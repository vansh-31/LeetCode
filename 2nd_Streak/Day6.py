# Problem : Palindrome Linked List
# Problem Statement : Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def check(l1, l2):
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next
            return l1 == None and l2 == None

        fast, prev, slow = head, None, head
        while fast and fast.next:
            fast = fast.next.next
            nextt = slow.next  # type: ignore
            slow.next = prev  # type: ignore
            prev = slow
            slow = nextt
        return check(prev, slow) or check(prev, slow.next)  # type: ignore
