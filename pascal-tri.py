# 4th March 2021 

'''
Problem: 
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = [[None]*x for x in range(1, numRows+1)]
        pascal[0] = [1]
        print(pascal)
        for i in range(1, numRows):
            pascal[i][0] = pascal[i][i] = 1
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal 
