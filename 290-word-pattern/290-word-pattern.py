class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        wpdict=dict()
        
        #예외 처리, s와 pattern의 길이 다르면 안됨.
        if len(s)!=len(pattern):
            return False
        
        
        for i in range(len(pattern)):
            if (pattern[i], s[i]) in wpdict.items():
                continue
            elif (pattern[i] in wpdict.keys()) or(s[i] in  wpdict.values()):
                return False
            else:
                wpdict[pattern[i]]=s[i]
        return True
            
        