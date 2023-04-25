class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        count = collections.Counter(nums)
        for common in count.most_common(k):
            output.append(common[0])
            
        return output