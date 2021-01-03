# Leetcode 
# 4th Jan 2021 

'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        Len = len(s.split())
        if (Len == 0):
            return 0
        else:            
            last = s.split()[Len - 1]
            return len(last)
