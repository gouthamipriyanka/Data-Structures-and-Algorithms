class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # Iterate over each bit in the number of the array
        for i in range(0,32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            ans  = ans | ((count % 3) << i)
        if ans > 2**31 -1:
            return ans - (1<<32)
        return ans
            