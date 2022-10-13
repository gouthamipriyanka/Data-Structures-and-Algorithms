class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        v1 = self.binarySearch(nums,target,True)
        v2 = self.binarySearch(nums,target,False)
        return[v1,v2]
        
    
    
    def binarySearch(self,nums,target,leftBias):
        length = len(nums)
        ans = -1
        low, high = 0,length-1
        while(low <= high):
            mid  = low + ((high-low)//2)
            if nums[mid] == target:
                ans = mid
                if leftBias:
                    high = mid-1
                else:
                    low = mid +1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid +1
        return ans
        
                    
                
                    