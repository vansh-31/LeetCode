# Problem : Swapping Nodes in a Linked List
# Problem Statement : You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n+=1
        temp = head
        beg_node = None
        for i in range(k-1):
            temp = temp.next
        beg_node = temp
        temp = head
        end_node = None
        for i in range(n-k):
            temp = temp.next
        end_node = temp
        beg_node.val,end_node.val = end_node.val,beg_node.val
        return head