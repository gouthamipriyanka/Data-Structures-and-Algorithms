#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
        if x == 1:
            return 1
    #Your code here
        low = 0
        high = x-1
        while(low <= high):
            mid = low + (high-low)//2
            sqr = mid*mid
            if sqr <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid -1
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends