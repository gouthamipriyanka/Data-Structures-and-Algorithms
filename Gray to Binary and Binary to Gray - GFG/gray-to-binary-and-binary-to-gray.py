#User function Template for python3

class Solution:
    
    def b_xor(self,a,b):
        return '1' if (a != b) else '0'
        
    def flip(self,c):
        return('0' if (c == '1') else '1') 
        
    def binToGrey(self, B):
        # code here 
        gray = ""
        gray += B[0]
        for i in range(1,len(B)):
            gray += self.b_xor(B[i-1],B[i])
        
        return gray
        
    def greyToBin(self, G):
         # code here 
        binary = ""
       
        binary += G[0]
        
        for i in range(1,len(G)):
           if (G[i] == "0"):
               binary += binary[i-1]
           else:
               binary += self.flip(binary[i-1])
               
        return binary
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        B = input()
        G = input()
        
        ob = Solution()
        print(ob.binToGrey(B))
        print(ob.greyToBin(G))
# } Driver Code Ends