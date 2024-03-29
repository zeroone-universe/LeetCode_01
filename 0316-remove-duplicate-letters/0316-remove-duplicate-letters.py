class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counter = collections.Counter(s)
        stack = []
        seen = []
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
                
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
                
            stack.append(char)
            if char not in seen:
                seen.append(char)
        
        return ''.join(stack)