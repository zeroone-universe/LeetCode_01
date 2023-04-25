class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        
        for idx in range(len(s)):
            length = 1
            while len(s) > idx+length and s[idx+length] not in s[idx:idx+length]:
                length += 1
                
            max_len = max(length, max_len)
            
        return max_len
            