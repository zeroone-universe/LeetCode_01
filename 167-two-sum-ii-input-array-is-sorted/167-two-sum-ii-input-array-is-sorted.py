class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(left, right, t):
            if left<=right:
                mid = left + (right - left)//2
            
                if numbers[mid] > t:
                    return binary_search(left, mid-1, t)
                elif numbers[mid] < t:
                    return binary_search(mid+1, right, t)
                else:
                    return mid
            return "fxck"
        
        
        for index1 in range(len(numbers)):
            output = binary_search(index1 + 1, len(numbers) - 1, target - numbers[index1])
            if type(output) == int:
                return [index1+1, output + 1]
            