class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        while(low <= high):
            mid = low + (high-low)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
        