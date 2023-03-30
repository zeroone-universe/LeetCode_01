class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                badack = stack.pop()
            
                if not len(stack):
                    break
            
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[badack]
                volume += distance * waters

            stack.append(i)

        return volume