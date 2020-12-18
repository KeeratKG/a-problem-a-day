# 18th Dec 2020 
# Leetcode 

'''
Given a roman numeral, convert it to an integer.
'''

# Solution 1 
class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Logic: 
        1. Create two cases: no on right is lesser than no on left and vice versa 
        2. If right > left, subtract left from right and add to value. Skip one position in loop. 
        3. If left > right, simply add value of left to total, and move to next in loop.  
       (Equality plays in for the last character of the string so no separate case required)
        '''
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0 # value of roman numeral 
        
        for i, n in enumerate(s):
            next_char = s[min((i+1, len(s)-1))]
            prev_char = s[max((i-1, 0))]
            
            # to skip the current character if it is greater than the one before it and so has already been added to val 
            if roman[prev_char] < roman[n]:   
                continue
                
            if roman[n] >= roman[next_char]:
                val += roman[n]
            else:
                val += roman[next_char]-roman[n]
        return val 
 
 # Solution 2 
 
class Solution:
    def romanToInt(self, s: str) -> int:
        intValue = 0
        romanLen = len(s) - 1
        i = 0
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        while i < romanLen:
            currentInt = values[s[i]]
            nextInt = values[s[i+1]]
            
            if currentInt in (1, 10, 100) and nextInt in (currentInt*5, currentInt*10):
                intValue += nextInt - currentInt
                i += 2
            else:
                intValue += currentInt
                i += 1
                
        if i == romanLen:
            intValue += values[s[i]]
        
        return intValue
