class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 1
        nums.sort()
        
        for i in nums:
            if i == 0:
                return 0
            elif i<0:
                answer*=-1
        
        return answer