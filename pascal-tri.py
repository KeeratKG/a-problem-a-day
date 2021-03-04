# 4th March 2021 

'''
Problem:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Fibonacci sequence generated as outputs 
        '''
        if n<3: 
            return n 
        
        prev1 = 2
        prev2 = 1 
        for stair in range(3, n+1): 
            if stair == n: return prev1 + prev2
            temp = prev1
            prev1 = prev1 + prev2 
            prev2 = temp
