class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i, tem in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<tem:
                last=stack.pop()
                output[last]=i-last
            stack.append(i)
            
        return output