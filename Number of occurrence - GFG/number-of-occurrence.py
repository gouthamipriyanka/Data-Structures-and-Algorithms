#User function Template for python3
class Solution:
    def count(self,arr, n, x):
		# code here
		first = self.occurence(arr,n,x,1)
		last = self.occurence(arr,n,x,0)
        
        if first == -1 and last == -1:
		    return 0
		else:
		    return (last-first)+1
		
    def occurence(self,arr,n,x,first):
		    low= 0
		    high = n-1
		    ans = -1
		    while(low <= high):
		        mid = low + ((high - low)//2)
		        mid_val = arr[mid]
		        if x == mid_val:
		            ans = mid
		            if first ==1:
		                high = mid -1
		            if first == 0:
		                low = mid + 1
		        elif x > mid_val:
		            low = mid +1
		        else:
		            high = mid -1
		    return ans       
	
		
		
		
		
		 
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends