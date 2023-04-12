class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dic = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        stack = []
        
        for bra in s:
            if bra in dic:
                stack.append(dic[bra])
            else:
                if not stack or stack.pop() != bra:
                    return False
                
        if stack:
            return False
        
        return True
