# Problem : Merge In Between Linked Lists
# Problem Statement : You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        tempA = tempB = list1
        while a > 1:
            tempA = tempA.next  # type:ignore
            a -= 1
        while b >= 0:
            tempB = tempB.next  # type:ignore
            b -= 1
        tempA.next = list2  # type:ignore
        while tempA and tempA.next:
            tempA = tempA.next
        tempA.next = tempB  # type:ignore
        return list1
