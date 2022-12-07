#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        # code here
        if N == 0:
            return 0
        digit = N%10
        sum = self.sumOfDigits(N//10) + digit
        return sum
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends