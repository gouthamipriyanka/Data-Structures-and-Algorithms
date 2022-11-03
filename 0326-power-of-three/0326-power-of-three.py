class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 1
        
        while(n > 1 and temp < n):
            temp = temp + (temp << 1)
        if temp == n:
            return True
        else:
            return False
        
        
        