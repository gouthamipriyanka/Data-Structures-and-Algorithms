class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        out  = []
        min_diff = inf
        for i in range(1,len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff < min_diff:
                min_diff = diff
                
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == min_diff:
                out.append([arr[i-1],arr[i]])
        
        return out
        
    
            
                
                
                