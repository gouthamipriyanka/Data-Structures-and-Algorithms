#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        if n == 0:
		    return 0
		power= (self.nearestpowerof2(n))
        res = 0
# 		res += ((1 << (nearestpowerof2-1))* nearestpowerof2)
# 		+((n-(1 << nearestpowerof2)) + 1)
# 		+self.countSetBits((n-(1 << nearestpowerof2)))
        res += (2**(power-1)*power)+(n - (2**power) + 1)+self.countSetBits(n -(2**power))
		
		return int(res)
		
	def nearestpowerof2(self,n):
	    nearest_power = 0
	    while((1 << nearest_power) <= n):
	        nearest_power+= 1
	    return (nearest_power - 1)
	        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends