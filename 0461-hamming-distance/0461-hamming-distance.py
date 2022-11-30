class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_x_y = x ^ y
        count = 0
        while(xor_x_y > 0):
            xor_x_y = xor_x_y & (xor_x_y - 1)
            count += 1
        return count
        