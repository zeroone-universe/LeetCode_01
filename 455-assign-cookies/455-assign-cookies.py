class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        s_idx = 0
        output = 0
        
        for gf in g:
            while s_idx < len(s):
                if gf <= s[s_idx]:
                    output+=1
                    s_idx += 1
                    break
                s_idx +=1
                
        return output