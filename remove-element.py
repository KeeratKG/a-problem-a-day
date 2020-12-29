# Leetcode 
# 30th Dec 2020 

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_ = 0
        
        if len(nums)==0:
            return 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[len_] = nums[i]
                len_ += 1
        return len_
