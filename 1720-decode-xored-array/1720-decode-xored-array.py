class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            first  = num ^ first
            arr.append(first)
        return arr
        
        
        