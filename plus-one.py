# 4th March 2021 

'''
Problem: 
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        Pay special attention to cases where the number of digits change 
        '''
        
        arr = []
        l = len(digits)
        i = 0
              
        num = ''
        for i in range(l):
            num += str(digits[i])
        num = int(num) + 1
        for i in range(len(str(num))):
            arr.append(str(num)[i])
        return arr
