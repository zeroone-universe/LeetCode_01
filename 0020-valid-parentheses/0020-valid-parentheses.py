class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []
        for idx in range(len(s)):
            if s[idx] in table:
                if not stack or table[s[idx]] != stack.pop():
                    return False
            else:
                stack.append(s[idx])

        if stack:
            return False
        
        return True