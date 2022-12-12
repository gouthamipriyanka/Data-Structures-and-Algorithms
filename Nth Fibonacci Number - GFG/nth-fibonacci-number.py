#User function Template for python3

class Solution:
    def nthFibonacci(self, n, a=0,b=1):
        # code here 
        # if n == 0 or n == 1:
        #     return n
        # else:
        #     return (self.nthFibonacci(n-1) + self.nthFibonacci(n-2))%1000000007
        
        if n-1 == 0:
            return b
        else:
            b,a = a+b,b
            return (self.nthFibonacci(n-1,a,b))%1000000007
            
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends