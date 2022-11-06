#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here - Using Right shift
        # count = 0
        # while(n > 0):
        #     if ((n & 1) != 0):
        #         break
        #     else:
        #         n = n >> 1
        #         count += 1
        # return count+1
        
        # Using Left Shift
        if n==0:
            return 0
        count = 0
        x = 1
        while(n):
            if ((n & x) != 0):
                break
            else:
                x = x << 1
                count += 1
        return count+1
        
                

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends