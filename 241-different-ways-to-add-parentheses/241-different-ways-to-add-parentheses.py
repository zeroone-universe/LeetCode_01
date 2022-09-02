class Solution:

    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left,right,value):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l)+value+str(r)))
            return results
            
        if expression.isdigit():
            return [int(expression)]
            
        
        
    
                    
            
        results = []
        for idx, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                
            
                results.extend(compute(left,right,value))
            
        return results
