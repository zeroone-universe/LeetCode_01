class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [[num for num in nums1 if num not in nums2], [num for num in nums2 if num not in nums1]]