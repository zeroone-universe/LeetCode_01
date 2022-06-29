class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        for _ in range(len(nums)-k+1):
            ans = heapq.heappop(heap)
            
        return ans