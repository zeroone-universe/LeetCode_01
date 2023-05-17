class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap_list = []
        for num in nums:
            heapq.heappush(heap_list, -num)
            
        for _ in range(k):
            output = heapq.heappop(heap_list)
            
        return -output