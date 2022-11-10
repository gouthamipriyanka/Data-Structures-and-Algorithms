class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x
        ans = -1
        if x == 0:
            return 0
        while(low <= high):
            mid = low + ((high-low)//2)
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                low = mid + 1
                ans = mid
            else:
                high = mid -1
        return ans
              
                
            
        