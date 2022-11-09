class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[idx]:
                ele = stack.pop()
                output[ele[0]] = idx-ele[0]

            stack.append([idx, temperatures[idx]])

        return output