class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        low = 0
        high = 0
        ans_list = []
        while(low <= len(nums1)-1 and high <= len(nums2)-1):
            if nums1[low] < nums2[high]:
                ans_list.append(nums1[low])
                low += 1
            else:
                ans_list.append(nums2[high])
                high += 1
       
        while(low <= len(nums1)-1):
            ans_list.append(nums1[low])
            low += 1
        
        while(high <= len(nums2)-1):
            ans_list.append(nums2[high])
            high += 1
            
        n = len(ans_list)
        print(ans_list[(n/2)-1])
        print(ans_list[((n/2)+1)-1])
        print(((ans_list[(n/2)-1])+ans_list[((n/2)+1)-1])/2)
        if n%2 == 0:
            return float(ans_list[(n/2)-1]+ans_list[((n/2)+1)-1])/2
        else:
            return ans_list[((n+1)/2)-1]