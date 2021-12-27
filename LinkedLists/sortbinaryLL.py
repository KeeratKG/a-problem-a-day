# problem statement 
'''
Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        # bruteforce: multiple passes of comparing all elements, in pairs 
        # while True:
        #     current = A 
        #     n = A.next 
        #     if current.val>n.val:
        #         current, n = n, current 
        #     A = A.next 

        # return A 

        # this method takes constant space but returns runtime error 


        # optimised 
        B = A  # B is a dummy pointer to the current node 
        noOfZeros,noOfOnes = 0,0
        while B:
            if B.val==0:
                noOfZeros+=1
            else:
                noOfOnes+=1
            B = B.next

        B = A  # come back to head node after traversing complete list once 

        while noOfZeros>0:
            B.val=0
            noOfZeros-=1
            B=B.next

        while noOfOnes>0:
            B.val=1
            noOfOnes-=1
            B=B.next
        
        return A
        
