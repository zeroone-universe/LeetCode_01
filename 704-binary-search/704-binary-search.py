class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        def binarysearch(nums, target, res):
            mid = len(nums)//2
            if len(nums) == 0:
                return -1
            elif nums[mid] == target:
                return len(nums)//2 + res
            elif nums[mid] < target:
                res += (mid+1)
                return binarysearch(nums[mid+1:], target, res)
            elif nums[mid] > target:
                return binarysearch(nums[:mid], target, res)
        return binarysearch(nums, target, 0)