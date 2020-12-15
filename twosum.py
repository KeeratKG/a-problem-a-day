# Leetcode
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={} #declare a dictionary to store v: index of v in nums 
        for i, v in enumerate(nums):
            remaining = target-v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []  #for completeness (in case a value does not exist in the array).May or may not be put here as question mentions that we can assume that there exists one solution. 
        
