class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        count = 0
        while(n>0):
            x = n & 1
            n = n>>1
            if (n & 1 == x):
                return False
            else:
                count = 0
        return True
            
        
    
   