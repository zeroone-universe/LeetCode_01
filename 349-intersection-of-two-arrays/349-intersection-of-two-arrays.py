class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(left, right, target):
            if left <= right:
                mid = left + (right - left)//2
                if nums2[mid] < target:
                    return binary_search(mid+1, right, target)
                elif nums2[mid] > target:
                    return binary_search(left, mid-1, target)
                else:
                    return target
            else:
                return "abc"
        
        
        nums1.sort()
        nums2.sort()
        
        output = []
        prev = "a"
        for num1 in nums1:
            if num1 == prev:
                continue
            
            yas = binary_search(0, len(nums2)-1, num1)
            if type(yas) == int:
                output.append(yas)
            
            prev = num1
            
        return output
        
        