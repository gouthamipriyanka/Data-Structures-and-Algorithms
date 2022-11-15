class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_n = n*(n+1)//2
        for i in range(len(nums)):
            sum_n = sum_n  - nums[i]
        return sum_n
        
        
            
        
            
        
        