class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            
            while(low < high):
                if (nums[low]+nums[high]+nums[i]) == 0:
                    triplet = [nums[low],nums[high],nums[i]]
                    if triplet not in ans:
                        ans.append(triplet)
                    low += 1
                    high -= 1
                elif (nums[low]+nums[high]+nums[i]) > 0:
                    high -= 1
                else:
                    low += 1
        return ans
        