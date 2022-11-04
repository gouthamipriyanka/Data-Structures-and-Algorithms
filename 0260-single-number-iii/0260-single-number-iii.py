class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[0]
        k = 0
        res1 = 0
        res2 = 0
        for i in range(1,len(nums)):
            res = res ^ nums[i]
        k = res &(~(res-1))
        for j in range(len(nums)):
            if (nums[j] & k) != 0:
                res1 = res1 ^ nums[j]
             
            else:
                res2 = res2 ^ nums[j]
             
        return [res1,res2]
        
            
        