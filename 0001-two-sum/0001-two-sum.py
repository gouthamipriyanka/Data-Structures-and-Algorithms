class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com_dict = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in com_dict:
                return [com_dict[nums[i]],i]
            else:
                com_dict[target - nums[i]] = i
            
        