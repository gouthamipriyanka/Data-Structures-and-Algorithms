#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        low = 0
        high = N-1
        while(low <= high):
            mid = low + (high-low)//2
            mid_val = arr[mid]
            if K == mid_val:
                return 1
            elif mid_val > K:
                high = mid -1
            else:
                low = mid + 1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends