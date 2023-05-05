class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_size = 0
        vowel = ['a','e','i','o','u']
        for cha in s[:k]:
            if cha in vowel:
                max_size+=1
        
        max_cur = max_size
        
        for idx in range(1, len(s)-k+1, 1):
            if s[idx-1] in vowel:
                max_cur-=1
            if s[idx+k-1] in vowel:
                max_cur += 1
                
            max_size = max(max_size, max_cur)
            
        return max_size
            