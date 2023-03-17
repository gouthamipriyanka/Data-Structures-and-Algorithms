class Solution:
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1
        
        return self.recursionString(s,low,high)
        
    def recursionString(self,s,low,high):
        if low >= high:
            return
        else:
            s[low],s[high] = s[high],s[low]
            
        low += 1
        high -= 1
        
        self.recursionString(s,low,high)
        
        
            
        
        