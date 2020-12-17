# 17th Dec 2020 
# Leetcode 

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
'''

# Solution using str()

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        r = 2 ** 31
        minLimit = r * -1 
        maxLimit = r - 1 
        
        status = False  #declares whether the given integer is a palindrome or not, set False by default 
                
        if x > minLimit and x < maxLimit: 
            if num == num[::-1]:
                status = True 
        return status 
        
        
# Solution without using str()

class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 2 ** 31
        minLimit = r * -1 
        maxLimit = r - 1 
        
        status = False  #declares whether the given integer is a palindrome or not, set False by default 
                
        if x < 0:
            status
            
        if x >= 0 and x < maxLimit: 
            num = x # store copy of x 
            rev = 0 # to store reverse 
          
        # will iterate as long as num is not zero
            while num:   
                '''
                1. remove last digit from original no 
                2. add it to the one's place in the reverse
                3. truncate the original and repeat the process 
                '''
                
                last = num % 10
                rev = rev * 10 + last 
                num = num // 10
            
            return x == rev
                
       

