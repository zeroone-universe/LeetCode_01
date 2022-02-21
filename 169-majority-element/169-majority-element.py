class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b=collections.Counter(nums)
        return b.most_common(1)[-1][0]