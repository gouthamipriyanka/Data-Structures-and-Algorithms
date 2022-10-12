class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f_count = {}
        for i in nums:
            f_count[i] = nums.count(i)
            if f_count[i] == 1:
                return i