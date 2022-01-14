# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,

# Given 1->1->2, return 1->2.

# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        seen = set() # set of seen elements 
        travel = A
        prev = None
        nxt = A.next
        while nxt: 
            # print(seen)
            if travel.val not in seen: 
                seen.add(travel.val)
                # print(travel.val, nxt.val)
                prev = travel 
                travel = nxt 
                nxt = nxt.next  
                # print(prev.val, travel.val, nxt.val)
            else:
                # print(prev.val, travel.val, nxt.val)
                travel = nxt 
                prev.next = travel 
                nxt = nxt.next 
                # print(prev.val, travel.val)
        if prev is not None: 
            if travel.val == prev.val:
                prev.next = nxt  
        return A

             



            

