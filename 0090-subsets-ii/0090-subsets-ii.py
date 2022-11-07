class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        size = pow(2,length)
        out1 = []
        out2 = []
        nums.sort()
        for i in range(0,size):
            for j in range(0,length):
                if(i & (1 << j) != 0):                  
                    out1.append(nums[j])
            if out1 not in out2:
                out2.append(out1)
            out1 = []
        return out2
                           
                
                    