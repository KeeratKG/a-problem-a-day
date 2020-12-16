# 16th Dec 2020
# Leetcode 

'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x: int) -> int:
        '''
        make separate cases for:
        - positive and negative integers
        - within 32 bit range and without 
        '''
        r = 2 ** 31
        maxLimit = r - 1
        minLimit = r * -1
        pos = True 
        
        if x<0:
            pos = False 
            x = x * -1
            
        y = str(x)
        n = len(y)
        space = ''
        for i in range(n):
            z = y[n-1-i]
            space = space + str(z)
        if pos == False and int(space)*-1 > minLimit:
            return int(space)*-1 
        elif pos == True and int(space) < maxLimit:
            return int(space)
        else:
            return 0
