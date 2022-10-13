class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [None] * size
        l = 0
        r  = size -1
        for i in nums:
            if i%2 == 0:
                res[l] = i
                l += 1
            else:
                res[r] = i
                r -= 1
        return res
                