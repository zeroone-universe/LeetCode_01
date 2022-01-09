class Solution:
    def isValid(self, s: str) -> bool:
        remain=[]
        table = {']':'[', ')':'(','}':'{'}
        
        for char in s:
            if char not in table:
                remain.append(char)
                
            else:
                if (not remain) or (remain.pop()!=table[char]) :
                    return False
                
        if len(remain)==0:
            return True
        else: return False