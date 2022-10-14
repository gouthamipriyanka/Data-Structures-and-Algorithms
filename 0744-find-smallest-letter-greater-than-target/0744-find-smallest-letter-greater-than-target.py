class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        low,high = 0,n-1
        while(low <= high):
            mid = low + (high-low)// 2
            if target < letters[mid]:
                high = mid -1
            else:
                low = mid + 1
            
        if low > n-1:
            return letters[0]
        else:
            return letters[low]