class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expend(left, right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        
        if len(s)<=1 or s == s[::-1]:
            return s
        
        result = ''
        
        for i in range(len(s)-1):
            result = max(
            result,
            expend(i, i+1),
            expend(i, i+2),
            key = len)
            
        return result