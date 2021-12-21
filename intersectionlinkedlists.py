# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        # brute force 

        # visited = set()
        # curA, curB = A, B 
        # while curA is not None: 
        #     visited.add(curA)
        #     curA = curA.next 

        # while curB is not None: 
        #     if curB in visited: 
        #         return curB
        #     else: 
        #         curB = curB.next 

        # return None 


        # another approach 
        curA, curB = A, B 
        a, b = 0, 0 # lengths of both linked lists 
        while curA is not None: 
            a += 1
            curA = curA.next 

        while curB: 
            b+=1 
            curB = curB.next 

        if a > b: 
            diff = a - b 
            curL = A 
            curS = B 
        else:
            diff = b - a 
            curL = B 
            curS = A 

        i = 0 
        while i<diff: 
            curL = curL.next 
            i += 1 

        while curL!=curS: 
            curL = curL.next 
            curS = curS.next 


        return curL 
    
    # most optimal approach, cleanest code 
        if A==None or B == None: 
            return None 

        a, b = A, B # dummy nodes 

        while a!=b:
            if a is None: 
                a = B 
            else: 
                a = a.next 

            if b is None: 
                b = A 
            else: 
                b = b.next 

        return a




        

