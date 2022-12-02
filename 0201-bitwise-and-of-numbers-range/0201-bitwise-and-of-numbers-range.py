class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count_right_shifts = 0
        while(left != right):
            
            left = left >> 1
            right = right >> 1
            count_right_shifts += 1
        return left << count_right_shifts
            
        
        