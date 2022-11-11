class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)== 1:
            return 0
        low = 0
        high = len(nums)-1
        if nums[low] > nums[low + 1]:
            return low
        if nums[high]> nums[high-1]:
            return high
        while(low <= high):
            mid = low + ((high-low)//2)
            mid_val = nums[mid]
            if mid_val > nums[mid+1] and mid_val > nums[mid-1]:
                return mid
            elif mid_val < nums[mid-1]:
                high = mid -1 
            else:
                low = mid + 1
        return -1
                