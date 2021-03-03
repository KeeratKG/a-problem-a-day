# 3rd March 2021 

'''
Problem Statement:

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

'''

# Solution 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1: return l2 
        if not l2: return l1 
        
        current = dummy = ListNode(0)
        while l1 and l2: 
            if l1.val < l2.val: 
                current.next = l1 
                l1 = l1.next 
            else: 
                current.next = l2 
                l2 = l2.next 
            current = current.next 
            
        if l1: current.next = l1 
        if l2: current.next = l2 
            
        return dummy.next 
        
