class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = low +(high-low)//2
            mid_element = nums[mid]
            if target == mid_element:
                return mid
            elif target > mid_element:
                low = mid +1
            else:
                high = mid-1
        return -1