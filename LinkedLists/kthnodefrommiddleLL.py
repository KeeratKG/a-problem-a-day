###
# Given a linked list A of length N and an integer B.

# You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

# If no such element exists, then return -1.
###

# brute force 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # brute force 

    def reverseList(self, A):
        prev = None 
        cur = A
        if cur.next is None:
            return A 

        while(cur is not None):
            nxt = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxt 

        self.head = prev 
        return self.head
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # length of linked list 
        length = 0 
        current = A 
        while current:
            current = current.next 
            length += 1
        # find the middle node, from the last element 
        if length%2 == 0: 
            middle = length//2 
        else: 
            middle = length//2 + 1 
        soln = Solution()
        last = soln.reverseList(A)
        # print(last.next.val)
        # # reach till the middle node first 
        i = 0 
        while i<middle-1:
            i += 1 
            last = last.next 

        # # traverse B nodes further from this node 
        # print(last.val)
        if (length-middle) >= B: 
            j = 0 
            while j<B:
                j += 1 
                last = last.next 
                # print(last.val)

            ans = last.val 
            return ans 

        else:
            return -1 
        
    # most obvious solution 
    # we need to print the n/2+1-B th element 
    def FindLength(self, A):
        # length of linked list 
        length = 0 
        current = A 
        while current:
            current = current.next 
            length += 1
        return length 

    def solve(self, A, B):
        soln = Solution()
        length = soln.FindLength(A)
        reqd_node = length//2 + 1 - B 
        if reqd_node <= 0:
            return -1 
        else: 
            i = 0 
            current = A
            while i<reqd_node-1:
                i += 1 
                current = current.next 

            return current.val 
