class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        size = pow(2,length)
        out2 = []
        out1 = []
        
        for i in range(0,size):
            for j in range(0,length):
                if (i & (1 << j)!= 0):
                    out1.append(nums[j])
            out2.append(out1)
            out1 = []
        return out2