class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0]*len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                date, _ = stack.pop()
                output[date] = (idx - date)
            stack.append((idx, temp))

        return output