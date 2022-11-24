class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Checking the number of times the element is occuring
        candidate = -1
        votes = 0
        for num in range(0,len(nums)):
            print(num)
            if votes == 0:
                candidate = nums[num]
                votes = 1
            else:
                if candidate == nums[num]:
                    votes+=1
                    print(votes)
                else:
                    votes -= 1
        print(votes)
        votes = 0
        print(candidate)
        
        # Checking if the number > N/2

        for num in range(0,len(nums)):
           
            if candidate == nums[num]:
                votes += 1
        if votes > (len(nums)//2):
            return candidate
       
        
        
            
        