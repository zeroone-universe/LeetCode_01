class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = max_len = 0
        used = {}
        
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char]+1
            else:
                max_len = max(max_len, idx-start+1) 
                
            used[char] = idx
        return max_len
            
#         used = {}
#         max_length = start = 0
#         for index, char in enumerate(s):
#             # 이미 등장했던 문자라면 `start` 위치 갱신
#             if char in used and start <= used[char]:
#                 start = used[char] + 1
#             else:  # 최대 부분 문자열 길이 갱신
#                 max_length = max(max_length, index - start + 1)

#             # 현재 문자의 위치 삽입
#             used[char] = index

#         return max_length
