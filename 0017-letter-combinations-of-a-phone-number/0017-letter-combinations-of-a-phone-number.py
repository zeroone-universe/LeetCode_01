class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        output = []
        
        def dfs(string, digits_dfs):
            if len(digits_dfs) == 0:
                output.append(string)
                return 0
            
            for alpha in dic[digits_dfs[0]]:
                dfs(string + alpha, digits_dfs[1:])
                
        
        dfs("", digits)
           
        return output 
        
            