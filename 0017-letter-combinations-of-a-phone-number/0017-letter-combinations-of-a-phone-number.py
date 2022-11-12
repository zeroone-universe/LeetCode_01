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
        
        def dfs(string, idx):
            if idx == len(digits):
                output.append(string)
                return 0
            
            for alpha in dic[digits[idx]]:
                dfs(string + alpha, idx+1)
                
        
        dfs("", 0)
           
        return output 
        
            