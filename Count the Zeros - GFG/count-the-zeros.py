#User function Template for python3

class Solution:
    def countZeroes(self, arr, n):
        # code here
        low = 0
        high = n-1
        ans = 0
        while(low <= high):
            mid = low +((high-low)//2)
            
            if arr[mid] == 1:
                low = mid + 1
            else:
                if (mid == 0 or arr[mid] != arr[mid-1]):
                    return (n-mid)
                else:
                    high = mid-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends