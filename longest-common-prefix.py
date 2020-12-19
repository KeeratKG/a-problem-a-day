# 19th Dec 2020 
# Leetcode 

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
''''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        logic: Compare each letter of the first word with corresponding letters of all subsequent words.
        IMPORTANT:
        - if strs is empty then strs[0] will give an Indexerror 
        - if strs has only one string (empty or otherwise), then return whole word 
        - there exist cases like [""], ["", ""]...
        '''
        
        # if not strs:
        #     return ""
        # elif len(strs) == 1:
        #     return strs[0]
        # elif len(strs) > 1:    
        #     for i in range(len(strs[0])):
        #         char = strs[0][i]   # The problem is when the strings are empty, when stored as a char they get stored as a null object. While if we just compare (as in the other solution), it works fine 
        #         for j in range(1, len(strs)):
        #             if char != strs[j][i]:
        #                 return strs[0][0:i] # consider answer as soon as first inequality encountered
    
        
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return p
