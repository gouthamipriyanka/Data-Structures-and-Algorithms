class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        result = []
        if l1 < l2:
            for i in range(l1):
                if nums1[i] in nums2:
                    if nums1[i] not in result:
                        result.append(nums1[i])
            return result
        else:
            for i in range(l2):
                if nums2[i] in nums1:
                    if nums2[i] not in result:
                        result.append(nums2[i])
            return result
                
                    