class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        def dfs(index, comb):
            if len(digits)==len(comb):
                result.append(comb)
                return
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, comb+j)
        
        dic={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        result=[]
        dfs(0,'')
        
        return result